from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
from .models import Match
import time


def fetch_upcoming_matches():
    options = Options()
    # Comment headless for debugging
    # options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    print("Opening CREX...")
    driver.get("https://crex.com/fixtures/match-list")

    # Wait for page or iframe
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "iframe"))
        )
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        if iframes:
            print(f"ℹ Found {len(iframes)} iframe(s), switching to first one...")
            driver.switch_to.frame(iframes[0])
    except:
        print("ℹ No iframe detected, continuing...")

    # Scroll to load matches
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(3):  # scroll 3 times
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Wait for match cards
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class*='match-card']"))
        )
        print("✅ Match cards detected!")
    except:
        print("⚠ Timeout: Match cards did not load.")
        driver.save_screenshot("debug_crex.png")
        with open("debug_crex.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        driver.quit()
        return

    # Parse HTML
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    match_cards = soup.select("div[class*='match-card']")

    count = 0
    for card in match_cards:
        teams = card.select("span[class*='team-name']")
        if len(teams) < 2:
            continue

        team_a = teams[0].get_text(strip=True)
        team_b = teams[1].get_text(strip=True)

        time_elem = card.select_one("span[class*='match-time']")
        match_time = None
        if time_elem:
            try:
                match_time = datetime.strptime(time_elem.get_text(strip=True), "%d %b %Y %I:%M %p")
            except:
                pass

        status_elem = card.select_one("span[class*='match-status']")
        status = status_elem.get_text(strip=True) if status_elem else "Upcoming"

        Match.objects.update_or_create(
            team_a=team_a,
            team_b=team_b,
            defaults={"start_time": match_time, "status": status}
        )

        print(f"📌 Saved: {team_a} vs {team_b} | Time: {match_time} | Status: {status}")
        count += 1

    print(f"✅ {count} matches updated successfully!")

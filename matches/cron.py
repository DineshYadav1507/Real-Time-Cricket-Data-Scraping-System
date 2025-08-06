from .scraping import fetch_upcoming_matches

def update_matches():
    print("Running scheduled match update...")
    fetch_upcoming_matches()
    print("Match update completed!")

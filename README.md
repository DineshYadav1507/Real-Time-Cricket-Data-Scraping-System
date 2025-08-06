# 🏏 Real-Time Cricket Data Scraping System

This project is a **real-time cricket data scraping and display system** built with **Django**, **Selenium**, and **BeautifulSoup**.  
It scrapes match data from [CREX](https://crex.com/) and stores it in a local database, displaying the results via a Django web interface.  
The system supports **manual scraping** or **automatic updates every X minutes**.

---

## 🚀 Features
- Fetch upcoming cricket matches from CREX
- Store matches in Django's database
- Display matches in a user-friendly web UI
- Auto-update every X minutes (no manual clicks)
- Screenshot & HTML saving for debugging
- Works cross-platform (Windows, macOS, Linux)

---

## 📦 Installation
1️⃣ Clone the Repository
```bash
git clone git@github.com:DineshYadav1507/Real-Time-Cricket-Data-Scraping-System.git
cd Real-Time-Cricket-Data-Scraping-System
2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install --upgrade pip
pip install -r requirements.txt
🛠 Database Setup
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
(Optional) Create a superuser:

bash
Copy
Edit
python manage.py createsuperuser
▶ Run the Development Server
bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

📡 Running the Scraper
Manual Run
Open Django shell:

bash
Copy
Edit
python manage.py shell
Run:

python
Copy
Edit
from matches.scraping import fetch_upcoming_matches
fetch_upcoming_matches()
Auto-Run Every X Minutes
We added a Django custom command for auto-running the scraper.
Run:

bash
Copy
Edit
python manage.py fetch_matches_loop --minutes 5
This will fetch matches every 5 minutes automatically.

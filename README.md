# Real-Time-Cricket-Data-Scraping-System


This Django-based project scrapes live cricket data from [CREX](https://crex.com/fixtures/match-list), stores it, and displays upcoming matches via a web UI.

## 📦 Features
- Real-time scraping (Scorecard, Live tabs)
- Django-admin support
- Background workers via Celery + Redis
- UI for match listings

## 🛠 Tech Stack
- Django
- Python
- Celery + Redis
- BeautifulSoup / Selenium (if needed)

## 🚀 How to Run Locally

```bash
git clone git@github.com:DineshYadav1507/Real-Time-Cricket-Data-Scraping-System.git
cd real-time-cricket-scraper
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

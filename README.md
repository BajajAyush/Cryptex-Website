<p align="center">
<img width="400" src="/static/logo_banner.svg"><br>
<h1 align="center"> Cryptex Cryptic Hunt</h1></p>

## Run Locally

To deploy this project
1.  Rename `.env.example` to `.env`
2.  Install the dependencies
    `pip install -r requirements.txt`
3.  Run database migrations
    `python manage.py migrate`
4.  Create superuser
    `python manage.py createsuperuser`
5.  Collect Static
    `python manage.py collectstatic`
6.  Load Admin panel customization data
    `python manage.py loaddata data.json`
7. Load extra settings data
    `python manage.py loaddata extrasettings.json`
8.  Run server
    `python manage.py runserver`
9. Visit Admin Panel at:
    http://127.0.0.1:8000/honeypot/


## Tech Stack

**Frontend:** TailwindCSS

**Server:** Python, Django

**Database:** SQLite



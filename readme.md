# 📱 Kotlite API

Kotlite (Angkot Elite) App: A Ridesharing Application for Optimising Vehicle Capacity to Decrease Traffic Congestion as one of Indonesia’s Priority Issues.
This application is a product of the Brillante Team (BA21-CAP0176) to fulfill the Capstone Project of Bangkit Academy 2021 led by Google, Gojek, Tokopedia, and Traveloka.

## 📌How to use

**1. Clone this repository by running the following command:**

```bash
git clone https://github.com/SVeeIS/kotliteProjectAPI.git
cd kotliteProjectAPI
```

**2. Configurasi database di kotliteProjectAPI/settings.py**

   If you want to run a local server then uncomment this part of the `settings.py`

```python
# UNCOMMENT THIS CODE FOR LOCAL TESTING
# Use a in-memory sqlite3 database when testing in CI systems
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
```

to be like this

```python
# UNCOMMENT THIS CODE FOR LOCAL TESTING
# Use a in-memory sqlite3 database when testing in CI systems
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**3. Install the required environment and enter virtualenv (recommendation)**

- Linux/macOS

```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

- Windows

```bash
python -m venv env
env\scripts\activate
pip install -r requirements.txt
```

**4. Run Django migrations to set up your models**

```bash
python manage.py makemigrations
python manage.py makemigrations drivers
python manage.py makemigrations passengers
python manage.py migrate
```

**5. Start a local web server:**

```bash
python manage.py runserver
```

In your browser, go to `http://localhost:8000/`

**6. Using the Django admin console**

- Create a superuser. You need to define a username and password:

```bash
python manage.py createsuperuser
```

- Start a local web server:

```bash
python manage.py runserver
```

In your browser, go to  `http://localhost:8000/admin` Log in to the admin site using the username and password you used when you ran createsuperuser.

**📌Documentation**

API documentation can be seen here (Coming Soon)
stay tuned (・ｗ・）

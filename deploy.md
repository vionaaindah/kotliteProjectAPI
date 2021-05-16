# Deploy to App Engine Standard

You can apply this application to the Google Cloud Platform App Engine. Following are the steps for running this application in a standard App Engine environment.

## 📌Setup Google Cloud Platform

**1. Open a Google Cloud Platform account.**

If you're new to Google Cloud, you can open <https://console.cloud.google.com/freetrial>, to create an account and new customers also get $300 in free credits to run, test, and deploy workloads.

**2. Select Project or create Project**

Open <https://console.cloud.google.com/projectselector2/home/dashboard> to select a project.

**3. Make sure that billing is enabled for your Cloud project**
Open <https://cloud.google.com/billing/docs/how-to/modify-project> to learn how to confirm that billing is enabled for your project.

**4. Enable the Cloud SQL Admin API**

Click <https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com> then select the project used

**5. Install and initialize the Cloud SDK**

Follow the installation instructions according to your operating system used <https://cloud.google.com/sdk/docs/install>

### 🔗Login ke gcloud

Acquire new credentials to use the Cloud SQL Admin API:
```bash
gcloud auth application-default login
```

## 📌Downloading and running the app

**1. Cloning the repository to local computer**

```bash
git clone https://github.com/SVeeIS/kotliteProjectAPI.git
```

**2. Open directory**

```bash
cd kotliteProjectAPI
```

## 📌Setup the local environment

### 🔗Installing the Cloud SQL Proxy

Follow the Cloud SQL Proxy installation steps according to the ones provided [here](https://cloud.google.com/sql/docs/mysql/quickstart-proxy-test#install-proxy)

### 🔗Creating a Cloud SQL instance

**1. Buat MySQL Second Generation instance melalui Cloud SQL**

Buat MySQL instance di <https://cloud.google.com/sql/docs/mysql/create-instance>

**2. Jalankan command ini untuk mendapatkan [CONNECTION_NAME]**

Ganti **[YOUR_INSTANCE_NAME]** dengan nama MySQL instance

```bash
gcloud sql instances describe [YOUR_INSTANCE_NAME]
```

**[CONNECTION_NAME]** memiliki format **[PROJECT_NAME]:[REGION_NAME]:[INSTANCE_NAME]**

### 🔗Inisiasi Cloud SQL instance

**1. Start Cloud SQL Proxy**

Gunakan **[CONNECTION_NAME]**
Untuk windows pastikan letak file yang didowload berada di root direktori aplikasi

- Linux/macOS

```bash
./cloud_sql_proxy -instances="[YOUR_INSTANCE_CONNECTION_NAME]"=tcp:3306
```

- Windows

```bash
cloud_sql_proxy.exe -instances="[YOUR_INSTANCE_CONNECTION_NAME]"=tcp:3306
```

**2. Buat user dan database Cloud SQL**

Buka <https://cloud.google.com/sql/docs/mysql/create-manage-users#creating> untuk membuat user, dan
Buka <https://cloud.google.com/sql/docs/mysql/create-manage-databases#create> untuk membuat database

## 📌Konfigurasi database settings

**Edit 'kotliteProjectAPI/settings.py'**

Uncomment bagian ini pada file `settings.py`

```python
# UNCOMMENT THIS CODE FOR SETUP IN GCP
# import pymysql  # noqa: 402
# pymysql.version_info = (1, 4, 0, 'final', 0)  # change mysqlclient version
# pymysql.install_as_MySQLdb()


# [START db_setup]
# if os.getenv('GAE_APPLICATION', None):
#     # Running on production App Engine, so connect to Google Cloud SQL using
#     # the unix socket at /cloudsql/<your-cloudsql-connection string>
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'HOST': '/cloudsql/[YOUR-CONNECTION-NAME]',
#             'USER': '[YOUR-USERNAME]',
#             'PASSWORD': '[YOUR-PASSWORD]',
#             'NAME': '[YOUR-DATABASE]',
#         }
#     }
# else:
#     # Running locally so connect to either a local MySQL instance or connect to
#     # Cloud SQL via the proxy. To start the proxy via command line:
#     #
#     #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
#     #
#     # See https://cloud.google.com/sql/docs/mysql-connect-proxy
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'HOST': '127.0.0.1',
#             'PORT': '3306',
#             'NAME': '[YOUR-DATABASE]',
#             'USER': '[YOUR-USERNAME]',
#             'PASSWORD': '[YOUR-PASSWORD]',
#         }
#     }
# [END db_setup]
```

menjadi seperti ini

```python
# UNCOMMENT THIS CODE FOR SETUP IN GCP
import pymysql  # noqa: 402
pymysql.version_info = (1, 4, 0, 'final', 0)  # change mysqlclient version
pymysql.install_as_MySQLdb()


# [START db_setup]
if os.getenv('GAE_APPLICATION', None):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/[YOUR-CONNECTION-NAME]',
            'USER': '[YOUR-USERNAME]',
            'PASSWORD': '[YOUR-PASSWORD]',
            'NAME': '[YOUR-DATABASE]',
        }
    }
else:
    # Running locally so connect to either a local MySQL instance or connect to
    # Cloud SQL via the proxy. To start the proxy via command line:
    #
    #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
    #
    # See https://cloud.google.com/sql/docs/mysql-connect-proxy
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': '[YOUR-DATABASE]',
            'USER': '[YOUR-USERNAME]',
            'PASSWORD': '[YOUR-PASSWORD]',
        }
    }
# [END db_setup]
```

Sesuaikan **[YOUR-CONNECTION-NAME], [YOUR-DATABASE], [YOUR-USERNAME], dan [YOUR-PASSWORD]** dengan yang telah dibuat.

Simpan `settings.py`

## 📌Jalankan aplikasi di Lokal komputer

**1. Set Up [Python environment](https://cloud.google.com/python/docs/setup), seperti Python, pip, dan virtualenv**

**2. Install requirements**

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

**3. Run Django migrations untuk set up models**

```bash
python manage.py makemigrations
python manage.py makemigrations drivers
python manage.py makemigrations passengers
python manage.py migrate
```

**4. Jalankan web server local**

```bash
python manage.py runserver
```

**5. Buka browser, jalankan <http://localhost:8000/>**

**6. Tekan `Control+C` untuk menghentikan web server local**

## 📌Menggunakan Django admin console

**1. Buat superuser, anda harus membuat username dan password**

```bash
python manage.py createsuperuser
```

**2. Jalankan web server local**

```bash
python manage.py runserver
```

**3 Buka <http://localhost:8000/admin> dibrowser anda dan login menggunakan username dan password yang telah anda buat tadi**

## 📌Deploy aplikasi

**1. Install gunicorn**

```bash
pip install gunicorn
```

**2. Kumpulkan semua konten static ke dalam satu folder**

```bash
python manage.py collectstatic
```

**3. Upload aplikasi**

```bash
gcloud app deploy
```

### 🔗Jalankan aplikasi

- melalui Cloud SDK

```bash
gcloud app browse
```

Jika browser tidak terbuka, klik link yang keluar di CLoud SDK.

- melalui Cloud Console

Klik link aplikasi yang tertera pada <https://console.cloud.google.com/appengine>

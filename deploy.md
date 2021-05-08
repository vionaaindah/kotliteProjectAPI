# Deploy to App Engine Standard

Aplikasi ini dapat anda deploy ke App Engine Google Cloud Platform. Berikut adalah langkah-langkah untuk menjalankan aplikasi ini di App Engine standard environment.

##  📌Menyiapkan Google Cloud Platform

**1. Buka akun Google Cloud Platform.**

Anda dapat membuat akun baru jika belum punya di <https://console.cloud.google.com/freetrial>, dan pelanggan baru akan mendapatkan $300 credit gratis.

**2. Pilih Project atau buat Project**

Buka <https://console.cloud.google.com/projectselector2/home/dashboard> untuk menentukan project

**3. Pastikan billing aktif untuk Project anda**

**4. Aktifkan Cloud SQL Admin API**

Klik <https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com> lalu pilih project yang dipakai

**5. Install dan inisialisasi Cloud SDK**
Ikuti instruksi instalasi sesuai dengan os anda di <https://cloud.google.com/sdk/docs/install>

### 🔗Login ke gcloud

```bash
gcloud auth application-default login
```


## 📌Download dan jalankan aplikasi

**1. Clone repositori ke Lokal komputer**

```bash
git clone https://github.com/SVeeIS/kotliteProjectAPI.git
```

**2. Buka direktori**

```bash
cd kotliteProjectAPI
```


## 📌Menyiapkan local environment

### 🔗Install Cloud SQL Proxy

Ikuti langkah instalasi Cload SQL Proxy sesuai dengan yang ada [di sini](https://cloud.google.com/sql/docs/mysql/quickstart-proxy-test#install-proxy)

### 🔗Membuat Cload SQL instance
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
python manage.py makemigrations polls
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

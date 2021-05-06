# Kotlite API

Kotlite adalah aplikasi ridesharing yang memungkinkan untuk pengemudi (driver) akan mendapatkan penumpang (rider) yang memiliki route atau jalur yang sama. Aplikasi ini merupakan produk dari Brillante Team (BA21-CAP0176) untuk memenuhi Bangkit Academy 2021 led by Google, Gojek, Tokopedia, and Traveloka Capstone Project.

## How to use

1. clone this repository with this code :

```bash
git clone https://github.com/SVeeIS/kotliteProjectAPI.git
cd kotliteProjectAPI
```

2. Configurasi database di kotliteProjectAPI/settings.py

3. Install environment yang dibutuhkan dan  masuk kedalam virtual env (rekomendasi)

```bash
virtualenv env
env\scripts\activate
pip install -r requirement.txt
```

4. jalankan Django migrations untuk set up models anda
```bash
python manage.py makemigrations
python manage.py makemigrations api
python manage.py migrate
```

5. Jalankan web server local
```bash
python manage.py runserver
```
Buka http://localhost:8000/ dibrowser anda

6. Menggunakan Django admin console
- Buat superuser, anda harus membuat username dan password
```bash
python manage.py createsuperuser
```
- Jalankan web server local
```bash
python manage.py runserver
```
Buka http://localhost:8000/admin dibrowser anda dan login menggunakan username dan password yang telah anda buat tadi

## Documentation

Dokumentasi API dapat dilihat disini (Coming Soon)

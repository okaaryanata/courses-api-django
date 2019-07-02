buat project baru :
python3 -m django startproject `nama project`
akan ada folder yg memiliki nama sama dengan nama project, saya ganti dengan nama app

cara run 
python3 manage.py runserver

cara buat module baru
python3 manage.py startapp `nama module` (contoh courses)
kemudian akan muncul folder sesuai dengan nama project

```
django bersifat modular bukan mvc, untuk setiap endpoint/menu (dalam project ini seperti courses) 
dia memiliki module sendiri", dimana isi didalam nya ada:
- model 
- view 
- apps
- admin
dll

```

migrate db
python3 manage.py migrate

seletelah menambahkan models baru untuk ke db, pastikan kita mendaftarkan 
model tersebut pada app/settings.py
lalu tambahkan 
'courses.apps.CoursesConfig',
pada installed_apps

setelah selesai, jalankan python3 manage.py makemigrations
setelah itu python3 manage.py migrate

ingat !!!
float di python adalah double di db

```
cara menggunakan virtual environtment
install terlebih dahulu virtualenv
pip3 install virtualenv
pada project kita, jalanankan
virtualenv nama_env
untuk menjalankan source nama_env/bin/activate
jika baru pertama kali, kita perlu membuat requirements.txt dan isikan apa saja yg diperlukan untuk menjalankan program
jika sudah maka jalankan
pip3 install -r requirements.txt
dan setelah itu untuk menjalankan program
python3 manage.py runserver
```

membuat admin page django


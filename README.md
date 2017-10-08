# Konekin - Tugas 1 Kelompok 10 Kelas B PPW 2017
## Anggota Kelompok
- Alya Putri - 1606836471
- Arga Ghulam Ahmad - 1606821601
- Claudio Yosafat - 1606917664
- Winayaka Ruhur Sandhya Pamungkas - 1606890561

## Status Aplikasi
[![pipeline status](https://gitlab.com/KelompokB10PPW2017/konekin/badges/master/pipeline.svg)](https://gitlab.com/KelompokB10PPW2017/konekin/commits/master)
[![coverage report](https://gitlab.com/KelompokB10PPW2017/konekin/badges/master/coverage.svg)](https://gitlab.com/KelompokB10PPW2017/konekin/commits/master)

## Link Heroku App
[https://konekin.herokuapp.com/](https://konekin.herokuapp.com/)

## Pembagian Tugas
- Alya Putri - profile page
- Arga Ghulam Ahmad - dashboard
- Claudio Yosafat - add friend
- Winayaka Ruhur Sandhya Pamungkas - update status

## Catatan Tambahan Antar Anggota Kelompok
1. Penggunaan 'base.html', 'footer.html & header.html', dan navbar.
```html
{% extends "base.html" %}
{% load staticfiles %}
{% load static %}
{% block content %}
{# isi content disini #}
{% endblock %}
```
2. Penggunaan app main.
	Untuk beberapa feature yang beririsan antar anggota gunakan app 'main'.
	Contoh :
	- 'models.py' digunakan untuk model profil yang digunakan hampir di setiap app.

3. Pengaturan urls app project konekin
    - dashboard menggunakan url(r'^stats/', ...)
    - update_status menggunakan url(r'^update-status/', ...)
    - halaman_profil menggunakan url(r^halaman-profil/' ...)
    - add_friend menggunakan url(r^add-friend/' ...)

4. Username dan password admin konekin
    Buka 'http://konekin.herokuapp.com/admin' atau 'localhost:8000/admin'.
    Masukkan username : 'adminkonekin' dan password : 'adminpass'.

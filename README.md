Nama : Nisyyah Azzahra
NPM : 2406495823
Kelas : PBP A

https://nisyyah-azzahra-activiagoodz.pbp.cs.ui.ac.id/

Cara mengimplementasikan checklist secara step-by-step
Membuat sebuah proyek Django baru:
    1. Membuat repositori git lokal kemudian hubungkan dengan repositori GitHub
    2. Membuat file requirements.txt yang berisi dependensi
    3. Instalasi Dependensi menggunakan pip install -r requirements.txt untuk menginstal dependensi yang diperlukan
    4. Menjalankan django-admin startproject activia_goodz . untuk membuat proyek Django baru

Membuat aplikasi dengan nama main pada proyek tersebut:
    1. Menjalankan python manage.py startapp main (Ini akan membuat direktori baru yang berisi struktur awal untuk aplikasi Django)
    2. Menambahkan aplikasi (main) ke INSTALLED_APPS pada settings.py


Melakukan routing pada proyek agar dapat menjalankan aplikasi main:
    1. Menambahkan rute URL (... path('', include('main.urls'))...) di urls.py pada direktori activia_goodz agar mengarah ke aplikasi main

Membuat model pada aplikasi main dengan nama Product dan memiliki 6 atribut wajib:
    1. Modifikasi models.py pada direktori main dengan
        class Product(models.Model):
            CATEGORY_CHOICES = [
                ('transfer', 'Transfer'),
                ('update', 'Update'),
            ]
            
            name = models.CharField(max_length=255)
            price = models.IntegerField()
            description = models.TextField()
            category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
            thumbnail = models.URLField(blank=True, null=True)
            is_featured = models.BooleanField(default=False)
            
            
            def __str__(self):
                return self.title
    2. Lakukan migrasi database (karena membuat perubahan pada models)

Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas:
    1. Membuat fungsi 
        def show_main(request):
        context = {
            'npm'   :'2406495823',
            'name'  :'Nisyyah Azzahra',
            'class' :'PBP A'
        }

        return render(request, "main.html", context)
        hal ini berguna untuk me-render tampilan main.html
    2. Modifikasi templates menjadi,
        <h5>NPM: </h5>
        <p>{{ npm }}</p>
        <h5>Name: </h5>
        <p>{{ name }}<p>
        <h5>Class: </h5>
        <p>{{ class }}</p> 

Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py:
    1. Menghubungkan main dengan fungsi yang sudah dibuat pada views.py dengan:
        app_name = 'main'

        urlpatterns = [
        path('', show_main, name='show_main')]

        --> Dengan begini ketika browser mengirim request ke server Django dia memeriksa urls.py level proyek. Ketemu path('', include('main.urls')) 
        --> Diteruskan ke urls.py aplikasi main. Lalu, Django memeriksa urls.py aplikasi main. Ketemu path('', show_main) 
        --> Jalankan fungsi show_main di views.py. Fungsi show_main mengambil data dan merender template HTML 
        --> Response dikirim balik ke browser.

Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat:
    1. Membuat projek baru pada PWS dengan nama projek activiagoodz
    2. Ubah Environs sesuai isi file .env.prod yang sudah dibuat
    3. Tambahkan URL deployment PWS pada ALLOWED_HOSTS. Pastikan format sesuai
    4. Lakukan git add, commit, kemudian push pws master 

Bagan request client ke web aplikasi berbasis Django beserta responnya 
(https://1.bp.blogspot.com/-u-n0WYPhc3o/X9nFtvNZB-I/AAAAAAAADrE/kD5gMaz4kNQIZyaUcaJJFVpDxdKrfoOwgCLcBGAsYHQ/s602/3.%2BPython%2BDjango%2B-%2BModul%2B2_Page2_Image5.jpg)

Alur request client ke web aplikasi berbasis Django 
    1. User akan request URL (misal: https://nisyyah-azzahra-activiagoodz.pbp.cs.ui.ac.id/). Request akan masuk ke dalam server Django dan diproses melalui urls proyek
    2. URL akan di konfigurasi dan akan diteruskan ke views yang sudah didefiniskan developer untuk memproses request tersebut
    3. Apabila proses membutuhkan database, maka views akan memanggil query models dan database akan me-return hasil dari query tersebut ke views
    4. Setelah request selesai diproses, hasil akan dipetakan ke dalam HTML yang sudah didefinisikan developer
    5. Template HTML akan dikirim ke browser dan browser akan menampilkan halaman web

Peran settings.py dalam proyek Django:
--> Sebagai konfigurasi utama dalam proyek Django
    Fungsi utama setting.py pada proyek activia-goodz:
        1. INSTALLED_APPS
            Menentukan daftar aplikasi (app) yang digunakan dalam proyek. Pada kasus ini jika ingin membuat app baru, misalnya main, maka bisa ditambahkan kesini. Django hanya akan mengenali aplikasi yang tercantum di sini.
        2. ALLOWED_HOSTS
            Menentukan domain atau IP yang diperbolehkan mengakses aplikasi. Pada kasus ini, untuk bisa membuka proyek pada PWS maka harus menambahkan "nisyyah-azzahra-activiagoodz.pbp.cs.ui.ac.id" kedalam daftar ALLOWED_HOSTS

Cara Kerja Migrasi Database di Django
Migrasi pada Django bertujuan untuk menyinkronkan perubahan model (models.py) dengan struktur database.
Ketika kita membuat perubahan pada model yang sudah ada, misal ingin menambahkan atribut stok pada Product di models.py. Maka diperlukan sinkronisasi dengan database. Sinkronisasi ini dilakukan dengan membuat file migrasi. Django memerlukan file migrasi yang berisi instruksi perubahan database. Hal ini dilakukan dengan menjalankan perintah python manage.py makemigrations. Django akan memindai semua aplikasi yang ada di INSTALLED_APPS dan mendeteksi perubahan model. 
Hasilnya: sebuah file migrasi baru di folder migrations/ setiap aplikasi
Setelah file migrasi dibuat, kemudian menjalankan python manage.py migrate maka Django akan membaca file migrasi dan mengeksekusi SQL ke database untuk mengubah struktur tabel sesuai perubahan model.

Alasan mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
    1. Menggunakan python
        Dengan menggunakan python, bisa lebih fokus memahami konsep pengembangan aplikasi tanpa harus memikirkan sintaks yang rumit
    2. Arsitektur MVT
        Saya pribadi merasa arsitektur MVT lebih jelas dan terstruktur jadi bisa lebih mudah dipahami
    3. Banyak fitur bawaan
        Bisa menggunakan banyak fitur bawaan tanpa harus install library tambahan
    4. Cukup aman
        Sistem autentikasi penggunanya menyediakan cara yang aman untuk mengelola akun dan kata sandi pengguna, sehingga meningkatkan keamanan pengguna.
    5. Open source dan gratis

Feedback untuk asisten dosen: Tidak ada, sudah cukup puas dengan mekanisme pengerjaan dan hasil tutorial 1
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
    Menambahkan rute URL (... path('', include('main.urls'))...) di urls.py pada direktori activia_goodz agar mengarah ke aplikasi main

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
    Menghubungkan main dengan fungsi yang sudah dibuat pada views.py dengan:
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

Data delivery dalam pengimplementasian sebuah platform
Data delivery tentu sangat diperlukan dalam pengimplementasian sebuah platform terutama untuk integrasi. Integrasi antar sistem pada suatu platform biasanya terdiri dari berbagai komponen yang perlu berkomunikasi. Data delivery berfungsi sebagai jembatan yang memungkinkan pertukaran informasi yang seamless antar sistem ini. Diantara manfaat lainnya adalah kita bisa mengakses data secara real-time secara sinkronus maupun asinkronus dengan data yang konsisten. Tanpa mekanisme data delivery, bisa terjadi ketidakkonsistenan data antara fitur yang berbeda, yang dapat menyebabkan error atau pengalaman pengguna yang buruk.

Beberapa alasan mengapa JSON lebih baik dan lebih populer daripada XML:
    
    
    1. JSON merupakan format yang ringan untuk menyimpan dan memindahkan data. JSON menggunakan sintaks yang minimal tanpa tagging yang dikhawatirkan terjadi redundansi. Bandwidth lebih efisien juga mengurangi beban transfer data, terutama untuk aplikasi mobile dan API.
    2. Format JSON secara cara penulisan/ sintaksis identik dengan kode untuk membuat JavaScript. Karena kesamaan ini, program JavaScript dapat dengan mudah mengonversi data JSON menjadi objek JavaScript asli. 
    3. Sintaks JSON diturunkan dari sintaks notasi objek JavaScript, tetapi format JSPN hanya berupa text. Kode untuk membaca dan menghasilkan data JSON dapat ditulis dalam bahasa pemrograman apapun.

Fungsi dari method is_valid() pada form Django
Method is_valid() berfungsi  memvalidasi data yang dikirimkan melalui form. ketika is_valid() metode yang menjalankan rutin validasi untuk semua kolomnya. Ketika metode ini dipanggil, jika semua kolom berisi data yang valid, metode tersebut akan return True dan menempatkan data form dalam atribut cleaned_data. Kemudian seluruh form akan ditampilkan seperti awal lagi. Jika is_valid() bernilai True, kita dapat menemukan semua data form yang tervalidasi dalam atribut cleaned_data. Kita dapat menggunakan data ini untuk memperbarui basis data atau melakukan pemrosesan lain. Dalam projek ini tentu kita membutuhkan method ini untuk membersihkan dan memvalidasi data yang masuk lewat form seperti name, price, description, category, thumbnail, is_featured dan form bisa siap dipakai lagi.


CSRF token
CSRF token adalah token yang berfungsi sebagai security. Token ini di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya (https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-2). Serangan bisa terjadi ketika situs web berbahaya berisi tautan, tombol formulir, atau JavaScript yang dimaksudkan untuk melakukan tindakan tertentu di situs web, menggunakan kredensial user yang masuk yang mengunjungi situs berbahaya tersebut di browser mereka. Jenis serangan terkait, 'login CSRF', di mana situs penyerang mengelabui browser user agar masuk ke situs dengan kredensial orang lain. CSRF token memastikan bahwa request yang dikirim benar-benar berasal dari form yang legitimate di website, bukan dari website penyerang. CSRF token juga memverifikasi bahwa request berasal dari domain yang sama dan dari form yang legitimate. Ketika kita tidak menambahkan CSRF token pada form Django penyerang bisa membuat page yang secara diam-diam mengirimkan request ke server kita menggunakan session user yang sedang login. Situs berbahaya berisi formulir tersembunyi atau kode JavaScript yang secara otomatis mengirimkan permintaan ke aplikasi Django target. Permintaan ini dirancang untuk melakukan tindakan yang diinginkan penyerang, seperti mengubah kata sandi, mentransfer dana, atau melakukan pembelian. Karena korban sudah diautentikasi dengan aplikasi Django (misalnya, memiliki kuki sesi yang valid), peramban mereka secara otomatis menyertakan kredensial autentikasi yang diperlukan dengan permintaan palsu. Aplikasi Django, yang tidak menyadari bahwa permintaan tersebut berasal dari sumber berbahaya, memproses permintaan tersebut seolah-olah sah, yang menyebabkan tindakan yang tidak diinginkan dilakukan atas nama korban.

Cara mengimplementasikan checklist secara step-by-step

    1. Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID. Ini dilakukan dengan membbuat fungsi baru yang menerima parameter request dengan nama bersesuaian dan membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada Product. Kemudian, Tambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML/JSON dan parameter content_type="application/xml" atau untuk JSON content_type="application/json".
    Untuk format XML by ID dan JSON by ID bisa dengan membuat fungsi baru yang menerima parameter request dan product_id dengan nama show_xml_by_id dan show_json_by_id. Kemudian, membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu. Kemudian, Tambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON). Bisa juga menambahkan blok try except pada fungsi untuk mengantisipasi kondisi ketika data dengan product_id tertentu tidak ditemukan dalam basis data. Jika data tidak ditemukan, kembalikan HttpResponse dengan status 404 sebagai tanda data tidak ada. Kemudian jangan lupa tambahkan import fungsi yang sudah dibuat pada urls.py yang ada didalam direktori main.
    
    2. Membuat routing URL untuk masing-masing views yang telah ditambahkan (XML, JSON, XML by ID, dan JSON by ID).
    Ini dilakukan dengan  import fungsi yang sudah dibuat sebelumnya kedalam file urls.py dalam direktori main. Kemudian, menambahkan path url masing-masing views ke dalam urlpatterns. 

    3. Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Read More" pada setiap data objek model yang akan menampilkan halaman detail objek. Ini dilakukan dengan menambahkan modifikasi kode pada main.html dalam direktori main/templates. Menggunakan tag template {% url %} untuk membuat link menuju view dengan nama main:create_ptoduct. Saat tombol diklik, user diarahkan ke halaman form tambah produk. Kemudian, menggunakan <p><a href="{% url 'main:show_product' product.id %}"><button>Read More</button></a></p> untuk menyediakan tombol Read More yang mengarahkan ke halaman detail produk (show_product) berdasarkan product.id.

    4. Membuat halaman form untuk menambahkan objek model pada app sebelumnya. Ini dilakukan dengan membuat file baru bernama forms.py untuk membuat struktur form yang dapat menerima data Product baru. Kemudian tambahkan fungsi untuk membuat dan menampilkan produk pada file views.py pada direktori main. Kemudian import fungsi-fungsi tadi dan tambahkan path URL dalam variabel urlpatterns.

    5. Membuat halaman yang menampilkan detail dari setiap data objek model. Ini dilakukan menambahkan 'products_list = Product.objects.all()' dan menambahkan list tsb pada context pada views.py dalam direktori main. Kemudian menambahkan path baru untuk create_product dan show_product pada urls.py dalam direktori main

screenshot hasil akses URL pada Postman:
ristek.link/screenshot-Postman-NA
backup link: https://drive.google.com/drive/u/0/folders/1J2ngWYLCyYoxhXoLfzPom5lo34Sv5n2A 
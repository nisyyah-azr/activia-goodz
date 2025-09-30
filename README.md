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

    5. Membuat halaman yang menampilkan detail dari setiap data objek model. Ini dilakukan menambahkan 'product_list = Product.objects.all()' dan menambahkan list tsb pada context pada views.py dalam direktori main. Kemudian menambahkan path baru untuk create_product dan show_product pada urls.py dalam direktori main

screenshot hasil akses URL pada Postman:
ristek.link/screenshot-Postman-NA
backup link: https://drive.google.com/drive/u/0/folders/1J2ngWYLCyYoxhXoLfzPom5lo34Sv5n2A 

Django AuthenticationForm
(kelebihan dan kekurangannya)


Django AuthenticationForm merupakan class bawaan Django yang digunakan untuk autentikasi (mengenali siapa yang akan login) berdasarkan username dan password user yang digunakan untuk proses login. Form ini menerima request sebagai argumen pertama dalam constructor-nya, kemudian data form jika berupa POST. AuthenticationForm punya dua field utama yaitu, username dan password. Selain validasi fieldnya, AuthenticationForm di dalam proses validasinya juga memanggil authenticate(...) dari Django untuk memeriksa apakah kredensial (username/password) yang dimasukkan valid lewat authentication backends. Django AuthenticationForm sudah built-in atau siap pakai, jadi developer tidak perlu membuat dari awal. Django menyediakan form ini, sudah meng-handle banyak aspek keamanan dan validasi dasar. Kemudian, sistem otentikasi dan middleware Django sudah terintegrasi. Karena sudah terintegrasi dengan authenticate(), login(), logout(), dan backends, sehingga lebih mudah dan aman secara default. Django AuthenticationForm juga tidak hanya memeriksa username/password, tetapi juga user yang non-aktif tidak bisa login (via confirm_login_allowed) — membantu menjaga keamanan/akses. Django AuthenticationForm juga tidak menyimpan password mentah, Ia melakukan hashing pada password user sehingga lebih aman. Namun, kekurangannya adalah sifatnya cukup kaku; jika aplikasi membutuhkan autentikasi dengan atribut khusus (misalnya login dengan NPM), developer perlu melakukan kustomisasi tambahan. 

Perbedaan Autentikasi dan Otorisasi


Autentikasi berfokus pada proses memverifikasi identitas pengguna (contohnya login dengan username dan password). Proses ini memverifikasi siapa yang mau login? apakah user valid? Sementara otorisasi berfokus pada pemberian izin setelah identitas terverifikasi. Contoh sederhana seperti nasabah bank yang sedang mengakses aplikasi mobile-banking, sebelum user mengakses aplikasi sistem harus memastikan apakah yang ingin masuk benar-benar nasabah terkait, hal ini dilakukan dalam proses login (autentikasi), kemudian jika berhasil login tentu sistem tidak akan memberikan semua data bank kepada nasabah terkait, bank hanya akan menampilkan fitur untuk nasabah inilah yang dinamakan otorisasi. Django mengimplementasikan autentikasi melalui User model, AuthenticationForm, serta fungsi seperti authenticate() dan login(). Untuk otorisasi, Django menyediakan sistem permissions dan groups, sehingga akses ke view atau objek tertentu dapat dikontrol berdasarkan aturan yang ditetapkan.

Kelebihan dan Kekurangan Session dan Cookies dalam Konteks Menyimpan State di Aplikasi Web


Session memiliki kelebihan karena data sensitif disimpan di server, sehingga lebih aman dan tidak bercampur antar pengguna meskipun menggunakan browser yang berbeda. Session juga memungkinkan penyimpanan state yang kompleks, seperti data login atau keranjang belanja. Namun, session membutuhkan manajemen tambahan di server sehingga bisa menambah beban jika jumlah pengguna banyak. Selain itu, session tetap berisiko diretas melalui serangan seperti session hijacking atau session forgery apabila session ID berhasil dicuri.
Cookie lebih sederhana dan ringan karena langsung disimpan di browser pengguna. Cookie cocok untuk menyimpan data seperti preferensi bahasa, tema, atau pilihan "remember me", dan dapat bersifat persistent sehingga mendukung penyimpanan jangka panjang. Akan tetapi, karena tersimpan di sisi client, cookie lebih rentan dimanipulasi maupun dicuri melalui serangan seperti Cross-Site Scripting (XSS). Oleh karena itu, cookie tidak aman digunakan untuk menyimpan informasi sensitif secara langsung.
Django menggabungkan keduanya. Data session tetap disimpan aman di server, sedangkan session ID dikirimkan ke client dalam bentuk cookie. Dengan cara ini, server dapat mengenali pengguna tanpa harus menyimpan data sensitif di browser, sehingga aplikasi web menjadi lebih aman sekaligus fleksibel dalam mengelola state pengguna.

Penggunaan Cookies 


Penggunaan cookies dalam pengembangan web tidak sepenuhnya aman secara default, terdapat beberapa risiko yang harus diwaspadai. Salah satu risikonya adalah penyimpanan informasi sensitif dalam bentuk clear text di dalam cookie, yang termasuk kategori Insecure Design menurut OWASP. Selain itu, cookies juga rentan dicuri melalui serangan Cross Site Scripting (XSS), di mana penyerang dapat menyisipkan kode berbahaya untuk mengambil session ID pengguna. Jika session ID ini jatuh ke tangan yang salah, akun pengguna bisa diambil alih. Persistent cookies yang disimpan dalam file komputer pengguna juga lebih berisiko dibanding session cookies yang hanya disimpan di memori browser, karena lebih mudah diakses atau dimodifikasi oleh program lain.
Django menangani risiko ini dengan beberapa mekanisme keamanan bawaan. Pertama, Django tidak menyimpan data sensitif langsung di cookie, melainkan hanya menyimpan session ID, sementara data utama disimpan aman di server melalui database session. Django juga memiliki proteksi Cross Site Request Forgery (CSRF) yang aktif secara default melalui CsrfViewMiddleware, sehingga hanya request sah yang akan diterima. Selain itu, Django melindungi aplikasi dari serangan XSS dengan melakukan escaping otomatis pada karakter berbahaya di dalam template. Django juga menyediakan opsi konfigurasi tambahan, seperti HttpOnly untuk mencegah akses cookie melalui JavaScript, Secure untuk memastikan cookie hanya dikirim lewat HTTPS, serta pengaturan masa berlaku cookie dengan SESSION_COOKIE_AGE. Dengan kombinasi ini, Django membantu meminimalisasi risiko keamanan dari penggunaan cookies dalam aplikasi web

Implementasi Autentikasi, Session, dan Cookies pada Django


    1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya. Menambahkan function maupun form yang diperlukan pada views.py seperti UserCreationForm, authenticate, login dan AuthenticationForm. Selanjutnya, buat html untuk register, dan login. Kemudian menambahkan function register dan login_user yang menggunakan request method post dan hubungkan dengan html yang bersesuaian. Kemudian import fungsi yang sudah dibuat tadi dan tambahkan path URL pada urls.py yang ada pada direktori main. Untuk membatasi akses halaman main dan product detail lalukan dengan menambahkan import login_required pada views.py, hal ini melakukan import decorator login_required dari sistem autentikasi milik Django. Tambahkan potongan kode @login_required(login_url='/login') di atas fungsi show_main dan show_product untuk mengimplementasikan decorator.

    2. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal. Setelah mengimplementasikan langkah-langkah pada poin 1, lakukan migrasi jalankan proyek Django dan buka http://localhost:8000/. Disini kita register akun yang ingin dimasukkan, login, kemudian tambahkan tiga produk. Sebelum lanjut, logout dulu dari akun sebelumnya kemudian ulangi langkah yang sama (register-login-tambahkan tiga produk).

    3. Menghubungkan model Product dengan User. Pertama, import User pada models.py, dan tambahkan user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) pada class Product. Kode tersebut berfungsi untuk menghubungkan satu product dengan satu user melalui sebuah relationship. Setiap product dapat terasosiasi dengan seorang user dengan many-to-one relationship. Kemudian, karena kita sudah melakukan perubahan pada model, lakukan migrasi. Kemudian tambahkan parameter commit=False pada function create_product agar Django tidak langsung menyimpan objek hasil form ke database. Dengan begitu, kita memiliki kesempatan untuk memodifikasi objek tersebut terlebih dahulu sebelum disimpan. Kemudian, tambahkan product_entry.user = request.user agar tiap objek yang dibuat akan secara otomatis terhubung dengan pengguna yang membuatnya.

    4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi. Untuk bisa menampilkan detail informasi pengguna yang sedang logged in seperti username menampilkan modifikasi show_main dengan menambahkan: 
    filter_type = request.GET.get("filter", "all")     
    if filter_type == "all":
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user)
    
    dan menambahkan:    'name'  : request.user.username, 'last_login': request.COOKIES.get('last_login', 'Never') pada context.
    
    Fungsi show_main menampilkan halaman utama setelah user login dan dilengkapi dengan filter product berdasarkan penulis. Filter ini diambil dari query parameter filter pada URL, dengan dua opsi: "my" untuk menampilkan hanya artikel yang ditulis oleh user yang sedang login, dan "all" untuk menampilkan semua artikel. Selain itu, informasi user seperti name diambil langsung dari username user yang sedang login. Kemudian filter "my" dan "all" yang disebutkan sebelumnya kita perlu menambahkan tombol filter tersebut pada main.html. Dan terakhir, tampilkan nama penulis di product_detail.html.

    Kemudian untuk menerapkan cookies seperti last_login pada halaman utama aplikasi pertama, pastikan sudah dalam keadaan logout. Tambahkan import HttpResponseRedirect, reverse, dan datetime di views.py. Kemudian, modifikasi function login_user untuk menyimpan cookie baru bernama last_login yang berisi timestamp terakhir kali pengguna melakukan login dengan menambahkan:
        - login(request, user) yang berfungsi untuk melakukan login menggunakan sistem autentikasi Django.
        - response = HttpResponseRedirect(reverse("main:show_main")) yang akan menetapkan redirect ke halaman main setelah response diterima.
        - response.set_cookie('last_login', str(datetime.datetime.now())) yang berfungsi untuk mendaftarkan cookie last_login di response dengan isi timestamp terkini. Kemudian tambahkan 'last_login': request.COOKIES['last_login'] ke dalam context di function show_main. Dan modifikasi fungsi logout_user untuk menghapus cookie last_login setelah melakukan logout. Terakhir tambahkan tombol logout untuk menampilkan data waktu terakhir pengguna login di main.html.

Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!


    Urutan dari paling tinggi ke paling rendah
    1. Inline styles (semua yang didalam style tag)
    2. ID selectors
    3. Classes selector
    4. Element selector

    Contoh:
        ...
        <h1 class="class1" style="color: red;" id="title1">HTML5 Example Page</h1> (Inline: prioritas 1, warna merah)
        ...
        style.css
        h1 {
        color: blue; (Element: prioritas 4, warna biru)
        }
        #title1 {
        color: aqua; (ID: prioritas 2, warna aqua)
        }
        .class1 {
        color: cadetblue; (Class: prioritas 3, warna cadetblue)
        }

    Ketika prioritas 1 tidak ada maka yang akan diambil adalah prioritas 2. Jika prioritas 2 tidak ada maka yang akan diambil adalah prioritas 3, dst.

Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

    Responsive design perlu diterapkan dalam pengembangan aplikasi web karena pengguna tidak hanya mengakses aplikasi melalui satu perangkat tetapi dari berbagai perangkat yang berbeda beda seperti, desktop, tablet, smartphone tentu perangkat tersebut memiliki ukuran layar, orientasi, dan resolusi yang berbeda. Tanpa responsive design, tampilan web akan berantakan, sulit dinavigasi, dan menurunkan pengalaman pengguna. Terdapat framework seperti Bootstrap  untuk membangun situs mobile-first dan responsive. Contoh aplikasi yang sudah menerapkan responsive design adalah  YouTube. Pada aplikasi mobile, YouTube memiliki navigation bar pada bagian bawah perangkat (misal, ketika menggunakan aplikasi YouTube lewat iPad), tetapi ketika YouTube dibuka lewat chrome menggunakan laptop, maka navigation bar berada di samping kiri layar dan terdapat logo garis tiga untuk meng-expand navigation bar. Contoh aplikasi yang belum menerapkan responsive design adalah https://www.websitesekolahgratis.web.id/. Ketika kita membuka website tersebut menggunakan handphone maka tulisan akan terlihat sangat kecil, karena design tidak menyesuaikan perangkat, tentu jelas berbeda ketika dibuka melalui desktop. Halaman akan tetap terlihat rapih.

Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

    Padding adalah ruang antara konten elemen dan border (gap antar konten dan border). Padding bisa di set untuk semua sisi sekaligus atau spesifik per sisi nya. 
    Border adalah garis yang mengelilingi padding sebuah elemen. Border bisa diatur ketebalan, style (misalnya solid, putus-putus), dan warnanya. Kita bisa membuat border sekaligus (mengelilingi elemen) atau menargetkan sisi tertentu secara spesifik.
    Margin adalah ruang transparan di luar border. Berfungsi untuk membuat jarak antara elemen tersebut dengan elemen lainnya pada suatu page. Jika padding memberi ruang di dalam kotak, margin memberi ruang di luar kotak. Sama seperti padding, margin bisa diatur untuk semua sisi atau per sisi.

Jelaskan konsep flex box dan grid layout beserta kegunaannya! (interaktif)

    Flexbox adalah model layout satu dimensi. bisa disusun berjajar ke samping (baris) atau ditumpuk ke atas (kolom), tetapi tidak keduanya sekaligus dalam satu aturan. Flexbox cukup fleksibel sehingga model ini sangat ideal untuk perataan, pengurutan, dan pendistribusian ruang di antara elemen dalam sebuah komponen perlu ditangani. Oleh karena itu, Flexbox sering diterapkan untuk komponen antarmuka berskala kecil, seperti navbar, galeri, atau kelompok tombol.
    Grid Layout ditujukan untuk penataan dalam dua dimensi, yaitu baris dan kolom secara bersamaan. Dengan Grid, sebuah struktur kisi-kisi yang presisi dapat didefinisikan untuk seluruh halaman, sehingga elemen-elemen besar seperti header, sidebar, dan area konten utama dapat diletakkan sesuai dengan keinginan dan tetap konsisten. Grid cukup diandalkan ketika ingin membuat sebuah tata letak halaman yang kompleks dan terstruktur. Pada praktiknya, kedua model ini sering digabungkan, di mana layout makro sebuah halaman disusun oleh Grid, sementara komponen-komponen di dalamnya dirapikan menggunakan Flexbox.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    Implementasikan fungsi untuk menghapus dan mengedit product.
    Pertama, membuat fungsi edit_product dan delete_product di views.py. Kemudian, buat file edit_news.html pada subdirektori main/templates untuk tampilan edit_product. Selanjutnya, import fungsi yang dibuat sebelumnya dan daftarkan url pattern pada urlpatterns di urls.py. Tambahkan tombol Edit dan Delete di edit_product.html dan card_product.html.

    Kustomisasi desain pada template HTML
    Menggunakan CSS untuk kustomisasi, ada 3 cara yaitu Inline style, Internal style sheet, dan External style sheet. Kemudian untuk merubah tampilan elemen tertentu, gunakan selector CSS (perlu diingat bahwa ada prioritas dalam memandang selector). Kemudian jangan lupa untuk integrasaikan pada django (menggunakan global.css)

    Kustomisasi halaman login, register, tambah product, edit product, dan detail product.
    Saya mengubah warna, bentuk, dan beberapa kalimat dari template yang disediakan pada tutorial. Warna tombol saya ubah dari hijau menjadi cyan dengan beberapa shade berbeda. Saya juga menambahkan hover transition color agar user bisa lebih jelas melihat tombol yang ingin di klik. Kemudian bentuk box-box yang tadinya tumpul saya jadikan block untuk mendapatkan hasil kotak agar lebih minimalis dan tegas. Untuk ini gunakan base template (base.html) agar navbar, CSS global, dan script bisa dipakai ulang.

    Kustomisasi halaman daftar product 
        Untuk menampilkan static files seperti gambar perlu diatur pada settings.py. Disini saya mengikuti tutorial untuk pengaturannya. Kemudian untuk menampilkan card dari product (jika product ada) buat html untuk card_product kemudian sambungkan dengan main.html. Saya pribadi mengubah style dari card dari tutorial sebelumnya dengan melakukan pengubahan warna pada tampilan kategori, kemudian bentuk tampilan yang tajam (block) kemudian untuk detail produk bisa dilihat dengan meng-klik block produk yang ingin dillihat tanpa menggunakan read more. 

    Pada tiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut
    Tambahkan tag <a> </a> yang berisi button yang ingin dibuat, dalam hal ini edit dan delete. Tambahkan pada card product agar tombol terlihat pada card

    Membuat navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop
    Saya menambahkan kategori navigation baru seperti women, men, kids, dan equipment yang mana merupakan kategori dari suatu produk yang sudah didefiniskan pada models.py. Hal ini dilakukan dengan menambahkan filter baru pada show_main dan menambahkan :
    untuuk tampilan desktop:
     <a href="{% url 'main:show_main' %}?filter={{ current_user_filter }}&category=[category nya]" class="text-gray-300 hover:text-white font-medium transition-colors"> [Nama pada Navbar]
          </a> 
    untuuk tampilan mobile:
    <a href="{% url 'main:show_main' %}?filter={{ current_user_filter }}&category=[category nya]" class="block text-gray-300 hover:text-white font-medium py-3 transition-colors"> [Nama pada Navbar]
          </a>
    pada navbar.html. sisanya mirip dengan yang ada pada tutorial
    
SISTEM PAKAR DIAGNOSIS KERUSAKAN KOMPUTER/LAPTOP

1. Inisialisasi Basis Pengetahuan
    Program dimulai dengan membangun Basis Pengetahuan menggunakan struktur data Dictionary. Di sini, setiap jenis kerusakan dimasukan ke dalam sekumpulan gejala unik yang disimpan dalam bentuk tuple. Penggunaan dictionary ini menjadikana pengelolaan data kerusakan dan solusi menjadi lebih terpusat, rapi, dan mudah untuk dikembangkan di masa mendatang.

2. Pemrosesan Input Pengguna
    Pada tahap interaksi, program menampilkan daftar gejala dan meminta pengguna memasukkan angka pilihan mereka. Input dari pengguna kemudian diproses melalui tahap parsing, di mana angka-angka tersebut diubah menjadi integer dan disimpan ke dalam sebuah Set. Penggunaan tipe data Set digunakan karena memungkinkan program melakukan perbandingan logika tanpa mempedulikan urutan angka yang dimasukkan oleh pengguna.

3. Mesin Inferensi dan Output
     Mesin Inferensi inig bekerja secara Forward Chaining. Program melakukan perulangan untuk mengecek setiap aturan di basis pengetahuan menggunakan fungsi issubset(). Jika semua gejala dalam suatu aturan ditemukan dalam input pengguna, sistem akan langsung menarik kesimpulan diagnosa dan menampilkan solusinya. Jika setelah semua aturan diperiksa tidak ada yang cocok, program secara otomatis menjalankan fungsi fallback untuk menginformasikan bahwa kerusakan tidak dikenali.
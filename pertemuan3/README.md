Tugas Praktikum - Implementasi Logika Fuzzy dengan Python

Repositori ini berisi penyelesaian tugas praktikum mata kuliah sistem pakar / kecerdasan buatan untuk mengimplementasikan Logika Fuzzy menggunakan bahasa pemrograman Python dan library `scikit-fuzzy`.

Persyaratan Sistem (Dependencies)
Pastikan Anda telah menginstal library yang dibutuhkan sebelum menjalankan program. Buka terminal atau command prompt, lalu jalankan:
```bash
pip install numpy scikit-fuzzy matplotlib

Terdapat dua studi kasus utama yang diselesaikan dalam repositori ini:

1. Sistem Kontrol Kipas Angin (fuzzy_kipas_angin.py)

    Sistem ini dirancang untuk menentukan kecepatan kipas angin secara otomatis berdasarkan kondisi suhu dan kelembapan ruangan.Input (Antecedents): Suhu (0-40 °C) dan Kelembapan (0-100 %).

    Output (Consequent): Kecepatan Kipas (0-100).Rule Base: Menggunakan 9 aturan (kombinasi 3x3) yang complete, sehingga sistem dapat memberikan output (defuzzifikasi Centroid) pada kondisi angka berapapun.
    
2. Kepuasan Pelayanan Masyarakat (fuzzy_pelayanan_masyarakat.py)

    Sistem ini digunakan untuk menilai tingkat kepuasan pengaduan masyarakat berdasarkan empat indikator penilaian.Input (Antecedents): Kejelasan Informasi, Kejelasan Persyaratan, Kemampuan Petugas, dan Ketersediaan Sarpras (Skala 0-100).

    Output (Consequent): Kepuasan Pelayanan (Skala 0-400).Analisis Kritis (Incomplete Rule Base): Pada skrip ini, telah diimplementasikan fungsi try-except (Error Handling). Hal ini ditujukan untuk membuktikan secara komputasional bahwa 13 Aturan (Rules) yang diberikan pada soal belum lengkap. Jika dimasukkan input tertentu (seperti pada contoh default di program), tidak ada rule yang bernilai > 0, sehingga sistem tidak dapat menghitung area defuzzifikasi.
    
    
Cara Menjalankan Program
    Buka terminal/CMD di direktori repositori ini, lalu jalankan perintah:
    Untuk studi kasus 1:Bashpython pertemuan3(1).py
    Untuk studi kasus 2:Bashpython pertemuan3(2).py
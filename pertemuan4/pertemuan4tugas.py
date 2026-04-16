def tampilkan_header():
    
    print(" === SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER/LAPTOP ===")
   
    print("Silakan pilih gejala yang dialami oleh komputer Anda.")

def main():
   
    daftar_gejala = {
        1: "Terdengar bunyi beep panjang berulang",
        2: "Layar blank hitam (no display)",
        3: "Sistem sering restart sendiri secara tiba-tiba",
        4: "Komputer mati mendadak tanpa peringatan",
        5: "Kipas menyala sebentar lalu mati lagi",
        6: "Lampu indikator power motherboard redup/berkedip",
        7: "Suhu laptop/PC terasa sangat panas ",
        8: "Kipas pendingin berbunyi sangat keras",
        9: "Mati tiba-tiba saat menjalankan program berat / game",
        10: "Muncul garis-garis atau warna aneh pada layar",
        11: "Sering mengalami Blue Screen of Death ",
        12: "Proses booting Windows sangat lambat",
        13: "Terdengar bunyi 'klik-klik' kasar pada penyimpanan",
        14: "Beberapa file tiba-tiba corrupt atau tidak bisa dibuka"
    }


    knowledge_base = {
        (1, 2, 3): {
            "kerusakan": "RAM Rusak / Kotor",
            "solusi": "Coba cabut RAM, bersihkan pin kuningan dengan penghapus pensil, lalu pasang kembali dengan kencang di slot yang berbeda jika ada."
        },
        (4, 5, 6): {
            "kerusakan": "Power Supply (PSU) Lemah / Rusak",
            "solusi": "Cek kabel power. Jika kabel normal, PSU kemungkinan tidak kuat mengangkat beban komponen. Pertimbangkan untuk mengganti PSU baru dengan daya yang sesuai."
        },
        (7, 8, 9): {
            "kerusakan": "Overheat pada Prosesor",
            "solusi": "Bongkar PC/Laptop, bersihkan debu tebal pada heatsink/kipas prosesor, dan ganti thermal paste yang sudah kering."
        },
        (2, 10): {
            "kerusakan": "VGA / Kartu Grafis Bermasalah",
            "solusi": "Cek suhu VGA dan update driver. Jika muncul artefak parah (garis-garis warna), kemungkinan chipset VGA rusak dan perlu diservis  atau diganti."
        },
        (11, 12, 13, 14): {
            "kerusakan": "Harddisk Corrupt / Rusak Fisik ",
            "solusi": "Segera backup data penting Anda ke tempat lain! Jalankan fitur Check Disk. Jika bunyi klik-klik terus berlanjut, segera ganti dengan SSD/HDD baru."
        }
    }

    tampilkan_header()

    for id_gejala, deskripsi in daftar_gejala.items():
        print(f"[{id_gejala}] {deskripsi}")
    
    print("-" * 60)
    
   
    input_user = input("Masukkan nomor gejala yang dialami (pisahkan dengan koma, contoh: 1,2,3): ")
    
    try:
       
        gejala_user = [int(x.strip()) for x in input_user.split(",")]
        gejala_user_set = set(gejala_user)
    except ValueError:
        print("\n[Error] Input tidak valid. Harap masukkan angka yang dipisahkan oleh koma.")
        return

   
    print("\n=== HASIL DIAGNOSA ===")
    

    
    diagnosa_ditemukan = False

    for rule_symptoms, info in knowledge_base.items():
       
        if set(rule_symptoms).issubset(gejala_user_set):
            print(f"Kerusakan: {info['kerusakan']}")
            print(f"Solusi Singkat: {info['solusi']}")
            diagnosa_ditemukan = True
            break 

    if not diagnosa_ditemukan:
        print("Kerusakan: Tidak dikenali")
        print("Solusi: Gejala yang dimasukkan tidak spesifik merujuk pada 5 kerusakan utama di sistem kami. ")

main()
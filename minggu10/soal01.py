def bandingkan(file01, file02):
    try:
        with open(file01, 'r', encoding='utf-8') as f1, \
             open(file02, 'r', encoding='utf-8') as f2:
            
            baris_f1 = f1.readlines()
            baris_f2 = f2.readlines()

        max_baris = max(len(baris_f1), len(baris_f2))

        perbedaaan = False
        print(f"{'='*20} Hasil Perbandingan {'='*20}")

        for i in range(max_baris):
            teks1 = baris_f1[i].strip() if i < len(baris_f1) else "[BARIS KOSONG]"
            teks2 = baris_f2[i].strip() if i < len(baris_f2) else "[BARIS KOSONG]"

            if teks1 != teks2:
                perbedaan = True
                print(f"Perbedaan pada Baris {i + 1}:")
                print(f"  File 1: {teks1}")
                print(f"  File 2: {teks2}")
                print("=" * 60)

        if not perbedaan:
            print("Kedua file identik. Tidak ada perbedaan ditemukan.")

    except FileNotFoundError as e:
        print(f"Kesalahan: File tidak ditemukan - {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

bandingkan('file01.txt', 'file02.txt')


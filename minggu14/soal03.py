def baca_file(nama_file):
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            isi_teks = file.read().lower()

            for tanda_baca in [".", ",", "!", "?", "\n", "\r"]:
                isi_teks = isi_teks.replace(tanda_baca, " ")
            
            kata_set = set(isi_teks.split())
            return kata_set
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan!")
        return None
    except Exception as e:
        print(f"Error: File '{nama_file}' tidak dapat dibaca! Detail: {e}")
        return None

def cari_kata():
    print("=== PROGRAM MENCARI KATA YANG SAMA DI DUA FILE ===")
    
    file1 = input("Masukkan nama file pertama: ")
    file2 = input("Masukkan nama file kedua: ")
    
    set_file1 = baca_file(file1)
    set_file2 = baca_file(file2)
    
    if set_file1 is not None and set_file2 is not None:
        kata_sama = set_file1.intersection(set_file2)
        
        print("\n== Hasil ==")
        if kata_sama:
            print(f"Ditemukan {len(kata_sama)} kata yang muncul di kedua file:")
            print(sorted(list(kata_sama)))
        else:
            print("Tidak ada kata yang sama di antara kedua file tersebut.")
cari_kata()

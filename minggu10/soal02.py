def kuis(nama_file):
    try:
        print(f"nama file1: {nama_file}")
        
        with open(nama_file, 'r', encoding='utf-8') as file:
            for baris in file:
                baris = baris.strip()
                
                if not baris or "||" not in baris:
                    continue
                
                bagian = baris.split("||")
                pertanyaan = bagian[0].strip()
                jawaban_benar = bagian[1].strip()

                print(pertanyaan)
                
                inputUser = input("Jawab: ")

                if inputUser.lower() == jawaban_benar.lower():
                    print("Jawaban benar!")
                else:
                    print("Jawaban salah!")
                
    except FileNotFoundError:
        print(f"Kesalahan: File '{nama_file}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

kuis('soal.txt')

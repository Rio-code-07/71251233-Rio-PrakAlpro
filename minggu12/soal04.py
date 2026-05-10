nama_file = input("Masukkan nama file : ")
hitung = {}
try:
    with open(nama_file) as f:
        for line in f:
            if line.startswith("From "):
                x = line.split()[1].split("@")[1]
                hitung[x] = hitung.get(x, 0) + 1
    urutan_soal = ['media.berkeley.edu', 'uct.ac.za', 'umich.edu', 'gmail.com', 'caret.cam.ac.uk', 'iupui.edu']
    hasil = {k: hitung[k] for k in urutan_soal if k in hitung}
    print(hasil)
except FileNotFoundError:
    print("File tidak ditemukan")
    

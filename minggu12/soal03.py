nama_file = input("Masukkan nama file : ")
try:
    handle = open(nama_file)
    x = dict()
    for baris in handle:
        if baris.startswith('From '):
            kata = baris.split()
            email = kata[1]
            x[email] = x.get(email, 0) + 1
    print(x)
except FileNotFoundError:
    print(f"File {nama_file} tidak ditemukan.")

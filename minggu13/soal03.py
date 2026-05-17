nama_file = input("Enter a file name: ")

try:
    handle = open(nama_file)
except FileNotFoundError:
    print(f"File tidak ditemukan: {nama_file}")
    exit()

distribusi_jam = dict()

for baris in handle:
    baris = baris.rstrip()
    if baris.startswith('From '):
        kata = baris.split()
        waktu = kata[5]
        jam = waktu.split(':')[0]
        distribusi_jam[jam] = distribusi_jam.get(jam, 0) + 1

list_jam = list(distribusi_jam.items())
list_jam.sort()

for jam, jumlah in list_jam:
    print(f"{jam} {jumlah}")

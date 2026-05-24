n = int(input('Masukkan jumlah kategori: '))

data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
    
    data_aplikasi[nama_kategori] = aplikasi

print("\nData Aplikasi")
print(data_aplikasi)

daftar_aplikasi_list = []

for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))

print("\nDaftar Aplikasi per Kategori")
print(daftar_aplikasi_list)

hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])

print("\nAplikasi yang muncul di semua kategori:")
print(hasil)

frekuensi_aplikasi = {}

for aplikasi_set in daftar_aplikasi_list:
    for nama_app in aplikasi_set:
        frekuensi_aplikasi[nama_app] = frekuensi_aplikasi.get(nama_app, 0) + 1

aplikasi_satu_kategori = {app for app, count in frekuensi_aplikasi.items() if count == 1}

print("\nAplikasi yang hanya muncul di satu kategori saja:")
print(aplikasi_satu_kategori if aplikasi_satu_kategori else "Tidak ada")

print(f"\nStatus pengecekan n > 2 (Nilai n saat ini = {n}):")
if n > 2:
    aplikasi_dua_kategori = {app for app, count in frekuensi_aplikasi.items() if count == 2}
    print(aplikasi_dua_kategori if aplikasi_dua_kategori else "Tidak ada\n")
else:
    print("Fitur dilewati boss, jumlah kategori tak lebih dari 2\n")



# Input
Gaji_per_jam = float(input("Masukkan gaji per jam: "))
Jumlah_jam_kerja = float(input("Masukkan jumlah jam kerja dalam 1 minggu: "))

# Perhitungan gaji 
Total_jam_kerja = Jumlah_jam_kerja * 5
Total_Gaji_Kotor = Gaji_per_jam * Total_jam_kerja

# Pajak 14%
Pajak = Total_Gaji_Kotor * 0.14
Total_Gaji_bersih = Total_Gaji_Kotor - Pajak

# Pengeluaran dari gaji bersih
Aksesoris_baju = Total_Gaji_bersih * 0.10 
Alat_tulis = Total_Gaji_bersih * 0.01      

# Sisa uang setelah pengeluaran
Sisa_uang = Total_Gaji_bersih - (Aksesoris_baju + Alat_tulis)

# Sedekah 25% dari sisa uang
Sedekah = Sisa_uang * 0.25

# Pembagian sedekah
Anak_yatim = Sedekah * 0.30  
Kaum_dhuafa = Sedekah * 0.70  

# Output
print("\n==OUTPUT==")
print("1. Pendapatan Budi sebelum melakukan pembayaran pajak: Rp", int(Total_Gaji_Kotor))
print("2. Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak: Rp", int(Total_Gaji_bersih))
print("3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp", int(Aksesoris_baju))
print("4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp", int(Alat_tulis))
print("5. Jumlah uang yang akan Budi sedekahkan: Rp", int(Sedekah))
print("6. Jumlah uang yang akan diterima anak yatim: Rp", int(Anak_yatim))
print("7. Jumlah uang yang akan diterima kaum dhuafa: Rp", int(Kaum_dhuafa))

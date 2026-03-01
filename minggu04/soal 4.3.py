inputUser = input("Masukan bulan (1-12): ")
try:
    bulan = int(inputUser)

    hasil = ("31" if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 9 or bulan == 11 else "30" if bulan == 4 or bulan == 6 or bulan == 8 or bulan == 10 or bulan == 12 else "28")
    print(hasil)    
except:
    print("bulan tidak valid!")

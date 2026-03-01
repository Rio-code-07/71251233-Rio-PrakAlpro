inputUser = input("Masukan bilangan: ")
try:
    bilangan = int(inputUser)

    hasil = ("Positif" if bilangan > 0 else "Negatif" if bilangan < 0 else "Nol")
    print(hasil)
except:
    print("Anda salah memasukkan input!")  
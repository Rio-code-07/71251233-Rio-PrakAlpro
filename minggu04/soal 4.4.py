inputUser1 = input("Masukan sisi: ")
inputUser2 = input("Masukan sisi: ")
inputUser3 = input("Masukan sisi: ")

try:
    sisi1 = int(inputUser1)
    sisi2 = int(inputUser2)
    sisi3 = int(inputUser3)

    hasil = ("3 sisi sama" if sisi1 == sisi2 == sisi3 else "2 sisi sama" if sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3 else "Tidak ada yang sama")
    print(hasil)
except:
    print("Input tidak valid!")



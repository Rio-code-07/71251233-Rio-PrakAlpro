tinggi = int(input("Masukan tinggi: "))
lebar = int(input("Masukan lebar: "))

angka = 1

for i in range(1, tinggi+1):
    for j in range(1, lebar+1):
        print(angka, end=" ")
        angka += 1
    print()


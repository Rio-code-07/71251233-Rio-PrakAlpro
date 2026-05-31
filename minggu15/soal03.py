def deret_ganjil(n):
    if n <= 0:
        return 0
    
    if n % 2 != 0:
        sisa = deret_ganjil(n-2)
        if sisa == 0:
            print(f"{n}", end="")
        else:
            print(f" + {n}", end="")
        return n + sisa
    else:
        return deret_ganjil(n - 1)

inputan = int(input("Masukan angka nya boss: "))
print(f"Deret Ganjil: ", end="")
hasil = deret_ganjil(inputan)
print(f" = {hasil}")

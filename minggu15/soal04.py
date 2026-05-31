def jumlah_digit(n):
    n = int(n)
    if n < 10:
        print(f"{n}", end="")
        return n
    
    digit_terakhir = n % 10
    sisa_digit = n // 10
    total_sebelumnya = jumlah_digit(sisa_digit)
    
    print(f" + {digit_terakhir}", end="")
    return total_sebelumnya + digit_terakhir

inputan = input("Masukkan bilangan boss: ")
print(f'"{inputan}" maka jumlah digitnya adalah ', end="")
hasil = jumlah_digit(inputan)
print(f" = {hasil}")

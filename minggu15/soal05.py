def kombinasi(n, r):
    if r == n:
        return 1
    if r == 0:
        return 1
    return  kombinasi(n - 1, r) + kombinasi(n - 1, r - 1)

n = int(input("Masukkan n: "))
r = int(input("Masukkan r: "))
 
if r > n:
    print("r tidak bisa lebih besar dari n boss")
else:
    hasil = kombinasi(n, r)
    print(f"C({n}, {r}) = {hasil}")



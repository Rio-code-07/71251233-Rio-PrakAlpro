def tiga_terbaik(bilangan):
    terbaik = sorted(bilangan, reverse=True)[:3]
    return terbaik

data = [13,28,35,22,78,11,90,27,100]
hasil = tiga_terbaik(data)

print(f"Data: {data}")
print(f"Tiga terbaik: {hasil}")
print(F"Peringkat 1: {hasil[0]}")
print(F"Peringkat 2: {hasil[1]}")
print(F"Peringkat 3: {hasil[2]}")
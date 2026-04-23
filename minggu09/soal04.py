import re

def cari_kata(kalimat):
    daftar_kata = re.findall(r'\w+', kalimat)

    if not daftar_kata:
        return None, None
    
    terpendek = min(daftar_kata, key=len)
    terpanjang = max(daftar_kata, key=len)

    return terpendek, terpanjang

teks = "red snakes, and a black frog in the pool."
pendek, panjang = cari_kata(teks)

print(f"Kalimat: {teks}")
print(f"Terpendek: {pendek}")
print(f"Terpanjang: {panjang}")



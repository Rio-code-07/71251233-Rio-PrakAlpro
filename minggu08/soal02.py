import re

def hitung_kata(kalimat, kata_dicari):
    
    kalimat = kalimat.lower()
    kata_dicari = kata_dicari.lower()
    pola = rf'\b{kata_dicari}\b'
    hasil = re.findall(pola, kalimat)
    return len(hasil)

teks = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
target = "makan"
jumlah = hitung_kata(teks, target)

print(f"Kalimat: {teks}")
print(f"Ditanyakan kata: {target} ")
print(f"Output: {target} ada {jumlah} buah")


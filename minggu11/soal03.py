with open("berita.txt", "r") as file:
    isi = file.read()
isi = isi.lower()
for tanda in [".", ",", "!", "?", ":", ";"]:
    isi = isi.replace(tanda, "")
semua_kata = isi.split()
kata_unik = sorted(set(semua_kata))

print(f"Total semua kata : {len(semua_kata)}")
print(f"Total kata unik  : {len(kata_unik)}")
print(f"\nDaftar kata unik :")
print(", ".join(kata_unik))


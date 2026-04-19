import re

def hapus_spasi(teks):
    teks_bersih = re.sub(r'\s+', ' ', teks).strip()
    return teks_bersih

teks_kotor = "saya tidak suka memancing ikan "
print(f'Output: "{hapus_spasi(teks_kotor)}"')


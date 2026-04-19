import re
from datetime import datetime

teks = """Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02)."""

pola = r'(\d{4})-(\d{2})-(\d{2})'
daftar_tanggal = re.findall(pola, teks)

sekarang = datetime.now()

print("Hasil:")
for i in daftar_tanggal:
    tahun, bulan, hari = i
    
    objek_tgl = datetime.strptime(f"{tahun}-{bulan}-{hari}", "%Y-%m-%d")
    selisih = (sekarang - objek_tgl).days
    tgl_format_baru = objek_tgl.strftime("%d-%m-%Y %H:%M:%S")
    
    print(f"{tgl_format_baru} selisih {selisih} hari")
    
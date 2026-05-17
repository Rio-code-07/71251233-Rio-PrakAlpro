data_diri = ('Mikael Gratianus Satrio Adi Kuncoro', '71251233', 'Prigi Wetan, Ketandan, Klaten utara, Klaten')
nama, nim, alamat = data_diri

print(f"\nData: {data_diri}\n")
print(f"{'NIM':<7}: {nim}")
print(f"{'NAMA':<7}: {nama}")
print(f"{'ALAMAT':<7}: {alamat}\n")

nim_tuple = tuple(nim)
print(f"NIM: {nim_tuple}\n")

nama_depan_saja = nama.split()[0]
nama_depan_tuple = tuple(nama_depan_saja)
print(f"NAMA DEPAN: {nama_depan_tuple}\n")

nama_terbalik_list = nama.split()[::-1]
nama_terbalik_tuple = tuple(nama_terbalik_list)
print(f"NAMA TERBALIK: {nama_terbalik_tuple}\n")

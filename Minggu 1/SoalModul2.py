# Data
harga1 = 650_000
harga2 = 685_000
harga3 = 715_000

gram1 = 25
gram2 = 15

# Pertanyaan pertama
modal1 = gram1 * harga1
untung1 = (gram1 * harga2) - modal1
persen1 = (untung1 / modal1) * 100

print("== JAWABAN PERTANYAAN PERTAMA ==")
print(f"Keuntungan (Rp): Rp {untung1}")
print(f"Keuntungan (%): {persen1:.2f} %")

# Pertanyaan kedua
totalGram = gram1 + gram2
modalTotal = modal1 + (gram2 * harga2)
untungTotal = (totalGram * harga3) - modalTotal
persenTotal = (untungTotal / modalTotal) * 100

print("\n== JAWABAN PERTANYAAN KEDUA ==")
print(f"Keuntungan (Rp): Rp {untungTotal}")
print(f"Keuntungan (%): {persenTotal:.2f} %")

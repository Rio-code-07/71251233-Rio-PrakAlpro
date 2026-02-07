import math

modalAwal = 200000000
targetCuan = 400000000
bunga = 0.10

waktu = math.log(targetCuan/ modalAwal) / math.log(1 + bunga)

print("\n==JAWABAN==")
print("Dibutuhkan waktu:",f"{waktu:.2f} tahun")
#input tinggi badan dan Body Mass Index
Tinggi_badan = float(input("Masukkan Tinggi Badan (m): "))
Body_Mass_Index = float(input("Masukkan BMI yang diharapkan: "))

#perhitungan 
Berat_badan = Body_Mass_Index * (Tinggi_badan ** 2)

#output
print("Berat badan yang diperlukan adalah", round(Berat_badan, 1), "kg")

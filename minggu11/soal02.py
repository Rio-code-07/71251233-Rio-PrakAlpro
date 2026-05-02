bilangan = []
print('Ketik "done" untuk melihat rata-rata.\n')
while True:
    inputan = input("Masukkan bilangan: ")
    if inputan == "done":
        print(f"Rata-rata: {sum(bilangan) / len(bilangan):.2f}")
        break
    else:
        bilangan.append(float(inputan))
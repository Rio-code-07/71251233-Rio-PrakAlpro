inputUser = input("Masukan suatu bilangan: ")
try:
    bilangan = int(inputUser)

    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    else:
        print("Nol")
except:
    print("Input tidak valid!")
    


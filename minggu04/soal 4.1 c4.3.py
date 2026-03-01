inputUser1 = input("Masukan bilangan pertama: ")
inputUser2 = input("Masukan bilangan kedua: ")
inputUser3 = input("Masukan bilangan ketiga: ")

try:
    bilangan1 = int(inputUser1)
    bilangan2 = int(inputUser2)
    bilangan3 = int(inputUser3)

    if bilangan1 > bilangan2 or bilangan1 > bilangan3:
        print("Terbesar:", bilangan1)
    elif bilangan2 > bilangan1 or bilangan2 > bilangan3:
        print("Terbesar:", bilangan2)
    elif bilangan3 > bilangan1 or bilangan3 > bilangan2:
        print("Terbesar:", bilangan3)
except: 
    print("Input tidak valid!")



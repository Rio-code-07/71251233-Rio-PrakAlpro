inputUser =  input("Masukkan suhu tubuh: ")
try:
    suhu = int(inputUser)
    if suhu >= 38:
        print("Anda demam") 
    else:
        print("Anda tidak demam")
except:
    print("Input tidak valid!")
    
n = int(input("Masukan Bilangan: "))
    
for i in range(n-1, 0, -1):
    prima = True
    for j in range(2, i-1):
        if i % j == 0: 
            prima = False 
    
    if prima == True:
        print("Maka prima terdekat <", n, "adalah", i)
        break

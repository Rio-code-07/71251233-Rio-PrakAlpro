def prima(n, i = None):
    if n <= 1:
        return False
    if i == None:
        i = n - 1
    if i == 1:
        return True
    if n % i == 0:
        return False
    
    return prima(n, i-1)

inputan = int(input("Masukin bilangannya boss: "))
if prima(inputan):
    print(f"{inputan} adalah bilangan prima")
else:
    print(f"{inputan} bukan bilangan prima")


    
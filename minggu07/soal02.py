import math
n = int(input("Masukan n: "))
    
for i in range(n, 0, -1):
    print(math.factorial(i), end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()



def palindrom(kalimat):
    kalimat = kalimat.replace(" ", "").lower()

    if len(kalimat) <= 1:
        return True
    if kalimat[0] == kalimat[-1]:
        return palindrom(kalimat[1:1])
    
inputan = input("Masukin kata nya boss: ")
if palindrom(inputan):
    print(f'"{inputan}" adalah palindrom')
else:
    print(f'"{inputan}" bukan palindrom')
    
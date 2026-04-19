import re 

def anagram(kata_pertama, kata_kedua):
    k1 = sorted(re.sub(r'[^a-z]', '', kata_pertama.lower()))
    k2 = sorted(re.sub(r'[^a-z]', '', kata_kedua.lower()))
    return k1 == k2

print(anagram("mata", "atma"))   
print(anagram("mata", "maat"))  
print(anagram("mata", "taam"))   
print(anagram("mata", "tama"))   

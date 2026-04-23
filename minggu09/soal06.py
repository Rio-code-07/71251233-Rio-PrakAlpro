import re, random, string

teks = """anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari"""

emails = re.findall(r'\S+@\S+', teks)
chars = string.ascii_letters + string.digits

print("Hasil:")
for email in emails:
    username = email.split('@')[0]
    pw = ''.join(random.choices(chars, k=8))
    
    print(f"{email} username: {username} , password: {pw}")
    
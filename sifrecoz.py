import os
from cryptography.fernet import Fernet

dosyalar = []

for dosya in os.listdir():
    if dosya == "sifrele.py" or dosya == "sifrecoz.py" or dosya == "anahtar.key":
        continue
    if os.path.isfile(dosya):
        dosyalar.append(dosya)
print(dosyalar)

with open("anahtar.key","rb") as anahtar_dosya:
	anahtar = anahtar_dosya.read()
print(anahtar)

for dosya in dosyalar:
	with open(dosya, "rb") as okunan_dosya:
		icerik = okunan_dosya.read()
	cozulen_icerik = Fernet(anahtar).decrypt(icerik)
	with open(dosya, "wb") as cozulen_dosya:
		cozulen_dosya.write(cozulen_icerik)
import string
import random

charlist = string.ascii_letters + string.punctuation + string.digits + " "

#print(charlist)

charlist = list(charlist)

#print(charlist)

key = charlist.copy()

#print(key)

random.shuffle(key)

#print(key)

plaintext = input("Enter a message to encrypt")

ciphertext = ""

#ENCRYPTION

for character in plaintext :

    pos = charlist.index(character)

    ciphertext += key[pos]

print(f"Original Message : {plaintext}")
print(f"Encrypted Message : {ciphertext}")


#DECRYPTION

ciphertext = input("Enter a message to decrypt:")
plaintext = ""

for character in ciphertext :

    pos = key.index(character)

    plaintext += charlist[pos]

print(f"Encrypted Message : {ciphertext}")
print(f"Original Message : {plaintext}")




#This will handle the aes cipher and this all will handle the decryption dn encryption side of the passwords
from Crypto.Cipher import AES
from Crypto.Random import random

def encryptingPlainText(plainText):
    #create a key for the aes
    key = random.getrandbits(128)

    #creates the aes encryption?
    cipher=AES.new(key, AES.MODE_ECB)

    #ensure the encrypted message is unique even if the same secret key is uses to prevent replay attacks
    # is when valid data transmission is used fraudulently or maliciously repeated
    nonce = cipher.nonce

    #this creates the actual ciphertext
    cipherText, tag = cipher.encrypt_and_digest(plainText)



"""
issues that need to be thought over and solved
first we will be encrypting the passwords so only one entry will be coming in first 
then we need to also apply salt so we need to incorporate that 
store salt
to see if we need the decrypt side because realistically if we encrypt and then compare then we will be able to tell if the program works the way intended without boiling it back to what it was???
this is gonna need a lot more research but defiantly a good idea to use pycryptodome 
would need to add it to requirements.txt as then people can load that with pip and get all teh needeed inputable library
"""
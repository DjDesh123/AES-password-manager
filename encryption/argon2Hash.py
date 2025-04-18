from argon2 import PasswordHasher

def HashingPassword(password):
    #initalises the password hasher
    ph = PasswordHasher()

    #hashes the password with salt
    #with aragon2 the salt is created automatically so i dont need to slice it 
    hash =ph.hash(password)

    #create salt
    salt = hash[:16]

    #combines them together
    enteredPassword = hash+salt

    #this needs to work in a way to check through the database then verify which could be a searching logarithm like binary search?
    ph.verify(hash,password)
from sqlalchemy import Table, Column, Integer, String, LargeBinary, MetaData
#metadata basically keeps the structure of the database as well as it allows the data to be manipulated while keeping the database intact and consisitent
#in short allows the table to be changed without breaking

def setupLoginDatabase():
    #initalises the metadata object
    metadataObj = MetaData()

    # creates the table and then labels what info will be in the table itself
    logInTable = Table(
        'LogInTable',
        metadataObj,
        # used nullable=False to prevenet empty data being put into the database
        # used LargeBinary as the password and salt are being stored in their binary form
        Column('id', Integer, primary_key=True),
        Column('username', String, nullable=False, unique=True),
        Column('encryptedPassword', LargeBinary, nullable=False),
        Column('salt', LargeBinary, nullable=False),
    )


    """
    from actual user authentication we should use one way (you can hash it but you can not reverse it)
    the plan will work as follows:
    if the user decides to create an account 
    we will use aragon2 to hash and salt the password 
    this is why we are storing a salt 
    then lets say a user is trying to log in the we will also encrypt the password and then instead of decrypting the encryped password stored in the database to the master password 
    it will only be encrypting to the level of the aragon2 which is one way 
    if they match allow access if they dont then deny
    
    
    
    the way the database is actually going to work is using AES encryption for extra level of safety
    so it will store the aes encrypted password that is encrypting the aragon2 for double layer of security 
    and we will store the salt for the aragon2
    then from this  when we need to find the key as the key is random we will use KDF (key derivation function) 
    this means we can find the randomise key and decrypt to the aragon2 hashed password
    which will be easy to compare as we can remove the two salts from either comparisons.
    """

    # need to remove the cipher.nonce it will screw things up
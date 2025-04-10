from sqlalchemy import Table, Column, Integer, String, LargeBinary, MetaData
#metadata basically keeps the structure of the database as well as it allows the data to be manipulated while keeping the database intact and consisitent
#in short allows the table to be changed without breaking

#initalises the metadata object
metadata_obj = MetaData()

# creates the table and then labels what info will be in the table itself
LogInTable = Table(
    'LogInTable',
    metadata_obj,
    # used nullable=False to prevenet empty data being put into the database
    # used LargeBinary as the password and salt are being stored in their binary form
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False, unique=True),
    Column('encrypted_password', LargeBinary, nullable=False),
    Column('salt', LargeBinary, nullable=False),
)
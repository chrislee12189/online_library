from pydoc import classname
from tokenize import Double
from main import db

class Author(db.model):
    #definte the name of the table in the database, name it authors
    __tablename__="authors"
    #setting up the columns for the table
    #set the primary key
    author_id=db.column(db.Integer, primary_key=True)
    name=db.column(db.String())
    country=db.Column(db.String())
    dob=db.Column(db.Date)
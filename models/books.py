from main import db

class Books(db.Model):
    #set table name as books
    __tablename__="books"
    book_id=db.Column(db.Integer, primary_key=True)
    title=db.column(db.String())
    genre=db.Column(db.String())
    length=db.Column(db.Integer())
    year=db.Column(db.Integer())
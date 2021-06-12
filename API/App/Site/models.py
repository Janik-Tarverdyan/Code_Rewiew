from Core import db


class User(db.Model):
    __tablename__ = 'Account_Users'

    # id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(128))
    Last_Name = db.Column(db.String(50))
    UserName = db.Column(db.String(50))
    eMail = db.Column(db.String(32))
    Password = db.Column(db.String(64))
    Permissions = db.Column(db.String(12))

from app import db
from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class User(db.Model, Serializer):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index= True, nullable=False)
    username = db.Column(db.String(50), index=True, nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

class Central(db.Model, Serializer):
    __tablename__ = 'centrals'

    id = db.Column(db.Integer, primary_key=True)
    device_UUID = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(20), index=True, nullable=False)

    def __init__(self, device_UUID, location):
        self.device_UUID = device_UUID
        self.location = location

class Peripheral(db.Model, Serializer):
    __tablename__ = 'peripherals'

    id = db.Column(db.Integer, primary_key=True)
    device_UUID = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, device_UUID, user_id):
        self.device_UUID = device_UUID
        self.user_id = user_id

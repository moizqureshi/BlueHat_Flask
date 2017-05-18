from app import db
from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class Users(db.Model, Serializer):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True, nullable=False)
    username = db.Column(db.String(25), index=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    firstName = db.Column(db.String(100), nullable=True)
    lastName = db.Column(db.String(100), nullable=True)
    registered = db.Column(db.DateTime, nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    admin = db.Column(db.Boolean, index=True, nullable=True)

    def __init__(self, email, username, password, firstName, lastName, registered, authenticated, admin):
        self.email = email
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.registered = registered
        self.authenticated = authenticated
        self.admin = admin

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_admin(self):
        return self.admin

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

class Central(db.Model, Serializer):
    __tablename__ = 'centrals'

    id = db.Column(db.Integer, primary_key=True)
    device_UUID = db.Column(db.Integer, nullable=False)
    locationName = db.Column(db.String(20), index=True, nullable=False)
    locationLatLong = db.Column(db.String(40), index=True, nullable=False)


    def __init__(self, device_UUID, locationName, locationLatLong):
        self.device_UUID = device_UUID
        self.locationName = locationName
        self.locationLatLong = locationLatLong

class Peripheral(db.Model, Serializer):
    __tablename__ = 'peripherals'

    id = db.Column(db.Integer, primary_key=True)
    device_UUID = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, device_UUID, user_id):
        self.device_UUID = device_UUID
        self.user_id = user_id

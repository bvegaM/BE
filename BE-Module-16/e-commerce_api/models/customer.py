from database import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phone_number = db.Column(db.String(10))

    def __init__(self, name, email, phone_number):
        self.id = None
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone_number
        }

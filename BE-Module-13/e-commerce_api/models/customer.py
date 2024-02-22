from database import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phone_number = db.Column(db.String(10))
    management = db.relationship('CustomerManagement',cascade="all, delete", uselist=False,lazy='noload')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone_number,
            'management': self.management.serialize() if self.management else None
        }

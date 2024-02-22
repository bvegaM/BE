from database import db

class CustomerManagement(db.Model):
    __tablename__ = "customer_managements"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))


    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'customer_id': self.customer_id
        }


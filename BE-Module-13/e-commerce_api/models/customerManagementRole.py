from database import db

class CustomerManagementRole(db.Model):
    __tablename__ = "customer_management_roles"

    id = db.Column(db.Integer, primary_key=True)
    customer_management_id = db.Column(db.Integer, db.ForeignKey('customer_managements.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
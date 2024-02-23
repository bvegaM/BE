from database import db

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'role_name': self.role_name
        }
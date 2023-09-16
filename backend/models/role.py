from database import db

class Role(db.Model):
    __tablename__ = 'role'
    role_name = db.Column(db.String(20), primary_key=True)
    role_desc = db.Column(db.Text, nullable=False)

    def json(self):
        return {
            'role_name': self.role_name,
            'role_desc': self.role_desc,
        }
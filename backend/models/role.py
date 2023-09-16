from database import db

class Role(db.Model):
    __tablename__ = 'role'
    role_name = db.Column(db.String(20), primary_key=True)
    role_desc = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Role {self.role_name} - {self.role_desc}>'


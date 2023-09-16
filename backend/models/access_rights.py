from database import db

class AccessRights(db.Model):
    __tablename__ = 'access_rights'
    access_right = db.Column(db.Integer, primary_key=True)
    user_role = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<AccessRights {self.access_right} - {self.user_role}>'

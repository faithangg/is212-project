import sys
sys.path.append('../../backend')

from database import db

class AccessRights(db.Model):
    __tablename__ = 'access_rights'
    access_id = db.Column(db.Integer, primary_key=True)
    access_control_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<AccessRights {self.access_id} - {self.access_control_name}>'
    
    
    def json(self):
        return {
            'access_id': self.access_id,
            'access_control_name': self.access_control_name
        }

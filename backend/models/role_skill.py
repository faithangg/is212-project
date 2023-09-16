from database import db

class RoleSkill(db.Model):
    __tablename__ = 'role_skill'

    role_name = db.Column(db.String(20), primary_key=True)
    skill_name = db.Column(db.String(50), primary_key=True)
    
    def __init__(self, role_name, skill_name):
        self.role_name = role_name
        self.skill_name = skill_name

    def json(self):
        return {
            'role_name': self.role_name,
            'skill_name': self.skill_name
        }
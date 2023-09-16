from database import db

class StaffSkill(db.Model):
    __tablename__ = 'staff_skill'

    staff_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(50), primary_key=True)
    
    def __init__(self, staff_id, skill_name):
        self.staff_id = staff_id
        self.skill_name = skill_name

    def json(self):
        return {
            'staff_id': self.staff_id,
            'skill_name': self.skill_name
        }

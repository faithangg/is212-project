from database import db

class JobApplication(db.Model):
    __tablename__ = 'job_application'

    application_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staff_id = db.Column(db.Integer, nullable=False)
    role_name = db.Column(db.String(20), nullable=False)
    application_date = db.Column(db.Date, nullable=False)
    
    def __init__(self, staff_id, role_name, application_date):
        self.staff_id = staff_id
        self.role_name = role_name
        self.application_date = application_date
        
    def json(self):
        return {
            'application_id': self.application_id,
            'staff_id': self.staff_id,
            'role_name': self.role_name,
            'application_date': self.application_date.strftime('%Y-%m-%d')
        }
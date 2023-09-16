from database import db

class LoginDetails(db.Model):
    __tablename__ = 'login_details'

    staff_id = db.Column(db.Integer, primary_key=True)
    staff_password = db.Column(db.String(255), nullable=False)

    def json(self):
        return {
            'staff_id': self.staff_id,
            'staff_password': self.staff_password
        }

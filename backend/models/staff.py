from database import db

class Staff(db.Model):
    __tablename__ = 'staff'
    staff_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staff_fname = db.Column(db.String(50), nullable=False)
    staff_lname = db.Column(db.String(50), nullable=False)
    dept = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    access_rights = db.Column(db.Integer, db.ForeignKey('access_rights.access_right'), nullable=False)

    def json(self):
        return {
            'staff_id': self.staff_id,
            'staff_fname': self.staff_fname,
            'staff_lname': self.staff_lname,
            'dept' : self.dept,
            'email': self.email,
            'access_rights': self.access_rights
        }

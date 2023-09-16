from database import db

class Staff(db.Model):
    __tablename__ = 'staff'
    staff_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staff_fname = db.Column(db.String(50), nullable=False)
    staff_lname = db.Column(db.String(50), nullable=False)
    dept = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    access_rights = db.Column(db.Integer, db.ForeignKey('access_rights.access_right'), nullable=False)

    def __repr__(self):
        return f'<Staff {self.staff_id} - {self.staff_fname} {self.staff_lname}>'

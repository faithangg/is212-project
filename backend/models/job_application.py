import sys
sys.path.append('../../backend')

from database import db

class JobApplication(db.Model):
    __tablename__ = 'job_application'

    application_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staff_id = db.Column(db.Integer, nullable=False)
    listing_id = db.Column(db.Integer, db.ForeignKey('role_listing.listing_id'), nullable=False)
    application_date = db.Column(db.Date, nullable=False)
    
    # Establish a relationship to retrieve the role listing associated with an application
    # role_listing = db.relationship('RoleListing', backref='applications')
        
    def json(self):
        return {
            'application_id': self.application_id,
            'staff_id': self.staff_id,
            'listing_id': self.listing_id,
            'application_date': self.application_date.strftime('%Y-%m-%d')
        }
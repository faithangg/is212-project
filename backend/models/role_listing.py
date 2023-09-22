from database import db

class RoleListing(db.Model):
    __tablename__ = 'role_listing'

    listing_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    deadline = db.Column(db.Date, nullable=False)

    applications = db.relationship('JobApplication', backref='role_listing')
    
    def json(self):
        return {
            'listing_id': self.listing_id,
            'role_name': self.role_name,
            'department': self.department,
            'category': self.category,
            'deadline': self.deadline.strftime('%Y-%m-%d')  # Format the date as a string if needed
        }
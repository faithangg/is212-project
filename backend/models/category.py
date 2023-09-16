from database import db

class Category(db.Model):
    __tablename__ = 'category'

    category = db.Column(db.String(20), primary_key=True)
    category_desc = db.Column(db.String(100), nullable=False)
    
    def __init__(self, category, category_desc):
        self.category = category
        self.category_desc = category_desc

    def json(self):
        return {
            'category': self.category,
            'category_desc': self.category_desc
        }

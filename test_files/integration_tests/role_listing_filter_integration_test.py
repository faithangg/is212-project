import unittest
import flask_testing
import json
import sys
import datetime
sys.path.append('../../backend')
from app import app
from database import db
from models.access_rights import AccessRights
from models.category import Category
from models.job_application import JobApplication
from models.login_details import LoginDetails
from models.role_listing import RoleListing
from models.role_skill import RoleSkill
from models.role import Role
from models.skills import Skill
from models.staff import Staff
from models.staff_skill import StaffSkill





class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://" # In-memory database
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {} 
    app.config['TESTING'] = True # Disable error catching during request handling

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCreateConsultation(TestApp):
    def test_filter_options(self):
        category = Category(category = "IT",category_desc ="information systems")
        staff = Staff(staff_id = 1, staff_fname = "john", staff_lname = "tan", dept = "it", email="johntan@email.com", access_rights=1) 
        db.session.add(category)
        db.session.add(staff)
        db.session.commit()

        response = self.client.get("/staff/filter_options",
                                    content_type='application/json')
        self.assertEqual(response.json, {'code': 200, 'data': {'category': ['IT'], 'department': ['it']}})


if __name__ == '__main__':
    unittest.main()

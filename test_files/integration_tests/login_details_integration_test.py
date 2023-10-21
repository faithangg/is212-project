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
        self.maxDiff = None

        staff = Staff(staff_id = 1, staff_fname = "john", staff_lname = "tan", dept = "IT", country="singapore", email="johntan@email.com", role=1) 
        login_details = LoginDetails(staff_id = 1, staff_password = "1234")

        db.session.add(staff)
        db.session.add(login_details)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestLoginDetails(TestApp):
    # Login successfully
    def test_login_success(self):
        response = self.client.get("/staff/login_details/1/1234")
        self.assertEqual(response.json, {'code': 201, 'access_id': 1})

    # Login unsuccessfully: wrong password
    def test_login_wrong_password(self):
        response = self.client.get("/staff/login_details/1/123")
        self.assertEqual(response.json, {'code': 500, 'data': "The password or staff id is incorrect"})

    # Login unsuccessfully: wrong staff id
    def test_login_wrong_password(self):
        response = self.client.get("/staff/login_details/2/1234")
        self.assertEqual(response.json, {'code': 500, 'data': "The password or staff id is incorrect"})





if __name__ == '__main__':
    unittest.main()

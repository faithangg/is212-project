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

        role_listing = RoleListing(listing_id = 1, role_name = "Software Engineer", category = "IT", department="IT", deadline = datetime.date(2024, 5, 17))
        role_listing2 = RoleListing(listing_id = 2, role_name = "Support Engineer", category = "IT", department="IT", deadline = datetime.date(2024, 5, 17))

        jobapplication1 = JobApplication(application_id = 1, staff_id = 1, listing_id = 1, application_date = datetime.date(2023, 5, 17))

        db.session.add(staff)
        db.session.add(login_details)
        db.session.add(role_listing)
        db.session.add(role_listing2)
        db.session.add(jobapplication1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestApplyRoles(TestApp):
    # Successful application
    def test_apply_role(self):
        request_body = {
            "staff_id" : 1,
            "listing_id" : 2
        }

        response = self.client.post("/staff/apply_for_role",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        actual_response_body = {
            "code": 200,
            "data": {
                'application': 
                {
                    'application_date': '2023-10-21',
                    'application_id': 2,
                    'listing_id': 2,
                    'staff_id': 1
                },
                'message': 'Successfully applied for the role!'
            }
        }
        

        self.assertEqual(response.json, actual_response_body)


    # Unsuccessful application: already applied
    def test_apply_role_unsuccessful(self):
        request_body = {
            "staff_id" : 1,
            "listing_id" : 1
        }

        response = self.client.post("/staff/apply_for_role",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        actual_response_body = {
            "code": 400,
            "data": {
                "message": "You have already applied for this role!"
            }
        }
        

        self.assertEqual(response.json, actual_response_body)





if __name__ == '__main__':
    unittest.main()

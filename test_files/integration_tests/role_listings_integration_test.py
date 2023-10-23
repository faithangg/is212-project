import unittest
import flask_testing
import json
import sys
from datetime import datetime, date
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
        staff1 = Staff(staff_id = 2, staff_fname = "olivia", staff_lname = "lim", dept = "Sales", country="singapore", email="olivialim@email.com", role=1) 


        category = Category(category = "IT",category_desc ="information systems")
        category1 = Category(category = "Finance",category_desc ="financial systems")


        role = Role(role_name = "Software Engineer", role_desc = "Develops software")
        role1 = Role(role_name = "Support Engineer", role_desc = "Supports software")

        role_listing = RoleListing(listing_id = 1, role_name = "Software Engineer", category = "IT", department="IT", deadline = date(2024, 5, 17))
        role_listing2 = RoleListing(listing_id = 2, role_name = "Support Engineer", category = "IT", department="IT", deadline = date(2024, 5, 17))

        
        role_skill1 = RoleSkill(role_name = "Software Engineer", skill_name = "Python")
        role_skill2 = RoleSkill(role_name = "Software Engineer", skill_name = "database management")
        role_skill3 = RoleSkill(role_name = "Software Engineer", skill_name = "scrum methodology")
        role_skill4 = RoleSkill(role_name = "Software Engineer", skill_name = "data structures and algorithms")

        role_skill5 = RoleSkill(role_name = "Support Engineer", skill_name = "Python")
        role_skill6 = RoleSkill(role_name = "Support Engineer", skill_name = "scrum methodology")
        role_skill7 = RoleSkill(role_name = "Support Engineer", skill_name = "data structures and algorithms")


        jobapplication1 = JobApplication(application_id = 1, staff_id = 1, listing_id = 1, application_date = date(2023, 5, 17))

        db.session.add(staff)
        db.session.add(staff1)
        db.session.add(role)
        db.session.add(role1)
        db.session.add(role_listing)
        db.session.add(role_listing2)
        db.session.add(category)
        db.session.add(category1)
        db.session.add(role_skill1)
        db.session.add(role_skill2)
        db.session.add(role_skill3)
        db.session.add(role_skill4)
        db.session.add(role_skill5)
        db.session.add(role_skill6)
        db.session.add(role_skill7)
        db.session.add(jobapplication1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestRoleListing(TestApp):
    def test_get_all_role_listings(self):
        response = self.client.get('/hr/role_listings')
        data = json.loads(response.data)
        
        # Assert the status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the response data matches what is expected
        expected_data = {
            "code": 200,
            "data": {
                "role_listing": [
                    {
                        "listing_id": 1,
                        "role_name": "Software Engineer",
                        "category": "IT",
                        "department": "IT",
                        "deadline": "2024-05-17",
                        "skills_required": ["Python", "database management", "scrum methodology", "data structures and algorithms"],
                        "role_desc": ["Develops software"]
                    },
                    {
                        "listing_id": 2,
                        "role_name": "Support Engineer",
                        "category": "IT",
                        "department": "IT",
                        "deadline": "2024-05-17",
                        "skills_required": ["Python", "scrum methodology", "data structures and algorithms"],
                        "role_desc": ["Supports software"]
                    }
                ]
            }
        }

        self.assertListEqual(sorted(data['data']['role_listing'][0]['skills_required']), sorted(expected_data['data']['role_listing'][0]['skills_required']))
        self.assertListEqual(sorted(data['data']['role_listing'][1]['skills_required']), sorted(expected_data['data']['role_listing'][1]['skills_required']))


    def test_get_one_role_listings_valid_id(self):
        response = self.client.get('/hr/role_listings/1')
        data = json.loads(response.data)

        # Assert the status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the response data matches what is expected
        expected_data = {
            "code": 200,
            "data": {
                "role_listing": {
                    "listing_id": 1,
                    "role_name": "Software Engineer",
                    "category": "IT",
                    "department": "IT",
                    "deadline": "2024-05-17",
                    "skills_required": ["Python", "database management", "scrum methodology", "data structures and algorithms"],
                    "role_desc": ["Develops software"]
                }
            }
        }

        self.assertListEqual(sorted(data['data']['role_listing']['skills_required']), sorted(expected_data['data']['role_listing']['skills_required']))

    def test_get_one_role_listings_invalid_id(self):
        response = self.client.get('/hr/role_listings/99') # Assume 99 is an invalid ID
        data = json.loads(response.data)

        # Assert the status code is 404
        self.assertEqual(response.status_code, 404)

        # Assert that the response data matches what is expected for an invalid ID
        expected_data = {
            "code": 404,
            "message": "There is not such role listing"
        }

        self.assertDictEqual(data, expected_data)

if __name__ == '__main__':
    unittest.main()
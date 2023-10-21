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
        staff1 = Staff(staff_id = 2, staff_fname = "olivia", staff_lname = "lim", dept = "Sales", country="singapore", email="olivialim@email.com", role=1) 


        category = Category(category = "IT",category_desc ="information systems")
        category1 = Category(category = "Finance",category_desc ="financial systems")


        role = Role(role_name = "Software Engineer", role_desc = "Develops software")
        role1 = Role(role_name = "Support Engineer", role_desc = "Supports software")

        role_listing = RoleListing(listing_id = 1, role_name = "Software Engineer", category = "IT", department="IT", deadline = datetime.date(2024, 5, 17))
        role_listing2 = RoleListing(listing_id = 2, role_name = "Support Engineer", category = "IT", department="IT", deadline = datetime.date(2024, 5, 17))

        
        role_skill1 = RoleSkill(role_name = "Software Engineer", skill_name = "Python")
        role_skill2 = RoleSkill(role_name = "Software Engineer", skill_name = "database management")
        role_skill3 = RoleSkill(role_name = "Software Engineer", skill_name = "scrum methodology")
        role_skill4 = RoleSkill(role_name = "Software Engineer", skill_name = "data structures and algorithms")

        role_skill5 = RoleSkill(role_name = "Support Engineer", skill_name = "Python")
        role_skill6 = RoleSkill(role_name = "Support Engineer", skill_name = "scrum methodology")
        role_skill7 = RoleSkill(role_name = "Support Engineer", skill_name = "data structures and algorithms")


        jobapplication1 = JobApplication(application_id = 1, staff_id = 1, listing_id = 1, application_date = datetime.date(2023, 5, 17))

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

class TestApplyRoles(TestApp):  
    # Create Role Listing Successful

    # Create Role Listing Unsuccessful: Deadline in the past

    # Create Role Listing Unsuccessful: Role Listing Exists

    # Create Role Listing Unsuccessful: Missing Required Fields

    # Get Role Skill For Role
    def test_role_skill(self):
        response = self.client.get("/hr/get_role_skills/Software Engineer",
                                    content_type='application/json')
        
        actual_response_body = {
            "skills_required": ['Python', 'data structures and algorithms', 'database management', 'scrum methodology' ]
        }
        

        self.assertEqual(response.json, actual_response_body)

    # Get Role Names
    def test_role_names(self):
        response = self.client.get("/hr/get_role_names",
                                    content_type='application/json')
        
        actual_response_body = ['Software Engineer', 'Support Engineer']

        self.assertEqual(response.json, actual_response_body)

    # Get Role Description
    def test_role_desc(self):
        response = self.client.get("/hr/role/Software Engineer/description",
                                    content_type='application/json')
        
        actual_response_body = {
            "description": ['Develops software']
        }
        

        self.assertEqual(response.json, actual_response_body)

    # Get Departments
    def test_role_desc(self):
        response = self.client.get("/hr/departments",
                                    content_type='application/json')
        
        actual_response_body = ['IT', 'Sales']
        

        self.assertEqual(response.json, actual_response_body)

    # Get Categories
    def test_role_categories(self):
        response = self.client.get("/hr/categories",
                                    content_type='application/json')
        
        actual_response_body = ['IT', 'Finance']
        

        self.assertEqual(response.json, actual_response_body)




if __name__ == '__main__':
    unittest.main()

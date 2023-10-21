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

class TesStaffDetails(TestApp):  
    # Get Staff Details: They have applied for a role
    def test_staff_apply_role(self):
        response = self.client.get("/staff/profile/1",
                                    content_type='application/json')
        
        actual_response_body = {
            'code': 200,
            'data': 
                {
                    'applied_roles': 
                    [
                        {
                            'role_listing': 
                            {
                                'category': 'IT',
                                'deadline': '2024-05-17',
                                'department': 'IT',
                                'listing_id': 1,
                                'role_name': 'Software Engineer'
                            },
                            'role_skill_match': 
                            {
                                'dont': ['Python', 'data structures and algorithms', 'database management', 'scrum methodology' ],
                                'have': [],
                                'match_percentage': '0'
                            }
                        }
                    ],
                    'staff_details':
                    {
                        'info':
                        {
                            'country': 'singapore',
                            'dept': 'IT',
                            'email': 'johntan@email.com',
                            'role': 1,
                            'staff_fname': 'john',
                            'staff_id': 1,
                            'staff_lname': 'tan'
                        },
                        'skills': []
                    }
            }
        }
        

        self.assertEqual(response.json, actual_response_body)

    # Get Staff Details: They did not apply for a role
    def test_no_roles_applied(self):
        response = self.client.get("/staff/profile/2",
                                content_type='application/json')
        
        actual_response_body = {
            'code': 200,
            'data': 
                {
                    'applied_roles': "No applied roles found for the given staff ID.",
                    'staff_details':
                    {
                        'info':
                        {
                            'country': 'singapore',
                            'dept': 'Sales',
                            'email': 'olivialim@email.com',
                            'role': 1,
                            'staff_fname': 'olivia',
                            'staff_id': 2,
                            'staff_lname': 'lim'
                        },
                        'skills': []
                    }
            }
        }
        
        self.assertEqual(response.json, actual_response_body)




if __name__ == '__main__':
    unittest.main()

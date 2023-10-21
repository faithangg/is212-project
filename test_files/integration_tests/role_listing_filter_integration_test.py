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

        category = Category(category = "IT",category_desc ="information systems")

        role = Role(role_name = "Software Engineer", role_desc = "Develops software")
        role1 = Role(role_name = "Support Engineer", role_desc = "Supports software")

        role_listing = RoleListing(listing_id = 1, role_name = "Software Engineer", category = "IT", department="IT", deadline = datetime.date(2024, 5, 17))
        role_listing2 = RoleListing(listing_id = 2, role_name = "Support Engineer", category = "IT", department="IT", deadline = datetime.date(2024, 5, 17))

        skill1 = Skill(skill_name = "Python", skill_desc = "programming language")
        skill2 = Skill(skill_name = "database management", skill_desc = "database management")
        skill3 = Skill(skill_name = "scrum methodology", skill_desc = "scrum methodology")
        skill4 = Skill(skill_name = "data structures and algorithms", skill_desc="data structures and algorithms")

        role_skill1 = RoleSkill(role_name = "Software Engineer", skill_name = "Python")
        role_skill2 = RoleSkill(role_name = "Software Engineer", skill_name = "database management")
        role_skill3 = RoleSkill(role_name = "Software Engineer", skill_name = "scrum methodology")
        role_skill4 = RoleSkill(role_name = "Software Engineer", skill_name = "data structures and algorithms")

        role_skill5 = RoleSkill(role_name = "Support Engineer", skill_name = "Python")
        role_skill6 = RoleSkill(role_name = "Support Engineer", skill_name = "scrum methodology")
        role_skill7 = RoleSkill(role_name = "Support Engineer", skill_name = "data structures and algorithms")


        staff_skill1 = StaffSkill(staff_id = 1, skill_name = "Python")
        staff_skill2 = StaffSkill(staff_id = 1, skill_name = "scrum methodology")
        
        db.session.add(role)
        db.session.add(role1)
        db.session.add(role_listing)
        db.session.add(role_listing2)
        db.session.add(category)
        db.session.add(staff)
        db.session.add(skill1)
        db.session.add(skill2)
        db.session.add(skill3)
        db.session.add(skill4)
        db.session.add(role_skill1)
        db.session.add(role_skill2)
        db.session.add(role_skill3)
        db.session.add(role_skill4)
        db.session.add(role_skill5)
        db.session.add(role_skill6)
        db.session.add(role_skill7)
        db.session.add(staff_skill2)
        db.session.add(staff_skill1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestRoleApplicantFilterandSort(TestApp):
    # Get all filter options
    def test_filter_options(self):
        response = self.client.get("/staff/filter_options",
                                    content_type='application/json')
        self.assertEqual(response.json, {'code': 200, 'data': {'category': ['IT'], 'department': ['IT']}})

    # Get filtered roles for all filter options [category, department, match percentage]
    def test_role_listing_filter_all(self):
        request_body = {
            'category': ["IT"],
            'department': ["IT"],
            'match_percentage': ['41-60']
        }

        response = self.client.post("/staff/filter_role_listings/1",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        actual_response_body = {
            "code": 200,
            "data": {
                "role_listings": [
                    {
                        "role_listing": {
                            "category": "IT",
                            "deadline": "2024-05-17",
                            "department": "IT",
                            "listing_id": 1,
                            "role_desc": "Develops software",
                            "role_name": "Software Engineer"
                        },
                        "role_skill_match": {
                            "dont": [
                                "data structures and algorithms",
                                "database management"
                            ],
                            "have": [
                                "Python",
                                "scrum methodology"
                            ],
                            "match_percentage": "50"
                        }
                    }
                ]
            }
        }

        self.assertEqual(response.json, actual_response_body)

    # Get filtered roles for category and department
    def test_role_listing_filter_cat_dept(self):
        request_body = {
            'category': ["IT"],
            'department': ["IT"],
            'match_percentage': []
        }

        response = self.client.post("/staff/filter_role_listings/1",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        actual_response_body = {
            "code": 200,
            "data": {
                "role_listings": [
                    {
                        "role_listing": {
                            "category": "IT",
                            "deadline": "2024-05-17",
                            "department": "IT",
                            "listing_id": 1,
                            "role_desc": "Develops software",
                            "role_name": "Software Engineer"
                        },
                        "role_skill_match": {
                            "dont": [
                                "data structures and algorithms",
                                "database management"
                            ],
                            "have": [
                                "Python",
                                "scrum methodology"
                            ],
                            "match_percentage": "50"
                        }
                    },
                    {
                        "role_listing": {
                            "category": "IT",
                            "deadline": "2024-05-17",
                            "department": "IT",
                            "listing_id": 2,
                            "role_desc": "Supports software",
                            "role_name": "Support Engineer"
                        },
                        "role_skill_match": {
                            "dont": [
                                "data structures and algorithms"
                            ],
                            "have": [
                                "Python",
                                "scrum methodology"
                            ],
                            "match_percentage": "67"
                        }
                    }
                ]
            }
        }
        

        self.assertEqual(response.json, actual_response_body)

    # Get filtered roles for  category and match percentage
    def test_role_listing_filter_cat_match_percentage(self):
        request_body = {
            'category': ["IT"],
            'department': [],
            'match_percentage': ['61-80']
        }

        response = self.client.post("/staff/filter_role_listings/1",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        actual_response_body = {
            "code": 200,
            "data": {
                "role_listings": [
                    {
                        "role_listing": {
                            "category": "IT",
                            "deadline": "2024-05-17",
                            "department": "IT",
                            "listing_id": 2,
                            "role_desc": "Supports software",
                            "role_name": "Support Engineer"
                        },
                        "role_skill_match": {
                            "dont": [
                                "data structures and algorithms"
                            ],
                            "have": [
                                "Python",
                                "scrum methodology"
                            ],
                            "match_percentage": "67"
                        }
                    }
                ]
            }
        }
        

        self.assertEqual(response.json, actual_response_body)

    # Get filtered roles for department, match percentage
    def test_role_listing_filter_dept_match_percentage(self):
        request_body = {
            'category': [],
            'department': ["IT"],
            'match_percentage': ['41-60']
        }

        response = self.client.post("/staff/filter_role_listings/1",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        actual_response_body = {
            "code": 200,
            "data": {
                "role_listings": [
                    {
                        "role_listing": {
                            "category": "IT",
                            "deadline": "2024-05-17",
                            "department": "IT",
                            "listing_id": 1,
                            "role_desc": "Develops software",
                            "role_name": "Software Engineer"
                        },
                        "role_skill_match": {
                            "dont": [
                                "data structures and algorithms",
                                "database management"
                            ],
                            "have": [
                                "Python",
                                "scrum methodology"
                            ],
                            "match_percentage": "50"
                        }
                    }
                ]
            }
        }
        

        self.assertEqual(response.json, actual_response_body)

    # Get filtered roles for category only
    def test_role_listing_filter_cat(self):
        request_body = {
            'category': ["IT"],
            'department': [],
            'match_percentage': []
        }

        response = self.client.post("/staff/filter_role_listings/1",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        actual_response_body = {
            "code": 200,
            "data": {
                "role_listings": [
                    {
                        "role_listing": {
                            "category": "IT",
                            "deadline": "2024-05-17",
                            "department": "IT",
                            "listing_id": 1,
                            "role_desc": "Develops software",
                            "role_name": "Software Engineer"
                        },
                        "role_skill_match": {
                            "dont": [
                                "data structures and algorithms",
                                "database management"
                            ],
                            "have": [
                                "Python",
                                "scrum methodology"
                            ],
                            "match_percentage": "50"
                        }
                    },
                    {
                        "role_listing": {
                            "category": "IT",
                            "deadline": "2024-05-17",
                            "department": "IT",
                            "listing_id": 2,
                            "role_desc": "Supports software",
                            "role_name": "Support Engineer"
                        },
                        "role_skill_match": {
                            "dont": [
                                "data structures and algorithms"
                            ],
                            "have": [
                                "Python",
                                "scrum methodology"
                            ],
                            "match_percentage": "67"
                        }
                    }
                ]
            }
        }
        

        self.assertEqual(response.json, actual_response_body)

    # Get filtered roles for department only
    def test_role_listing_filter_dept(self):
        request_body = {
            'category': [],
            'department': ["IT"],
            'match_percentage': []
        }

        response = self.client.post("/staff/filter_role_listings/1",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        actual_response_body = {
            "code": 200,
            "data": {
                "role_listings": [
                    {
                        "role_listing": {
                            "category": "IT",
                            "deadline": "2024-05-17",
                            "department": "IT",
                            "listing_id": 1,
                            "role_desc": "Develops software",
                            "role_name": "Software Engineer"
                        },
                        "role_skill_match": {
                            "dont": [
                                "data structures and algorithms",
                                "database management"
                            ],
                            "have": [
                                "Python",
                                "scrum methodology"
                            ],
                            "match_percentage": "50"
                        }
                    },
                    {
                        "role_listing": {
                            "category": "IT",
                            "deadline": "2024-05-17",
                            "department": "IT",
                            "listing_id": 2,
                            "role_desc": "Supports software",
                            "role_name": "Support Engineer"
                        },
                        "role_skill_match": {
                            "dont": [
                                "data structures and algorithms"
                            ],
                            "have": [
                                "Python",
                                "scrum methodology"
                            ],
                            "match_percentage": "67"
                        }
                    }
                ]
            }
        }
        

        self.assertEqual(response.json, actual_response_body)

    # Get filtered roles for match percentage only
    def test_role_listing_filter_match_percentage(self):
        request_body = {
            'category': [],
            'department': [],
            'match_percentage': ['41-60']
        }

        response = self.client.post("/staff/filter_role_listings/1",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        actual_response_body = {
            "code": 200,
            "data": {
                "role_listings": [
                    {
                        "role_listing": {
                            "category": "IT",
                            "deadline": "2024-05-17",
                            "department": "IT",
                            "listing_id": 1,
                            "role_desc": "Develops software",
                            "role_name": "Software Engineer"
                        },
                        "role_skill_match": {
                            "dont": [
                                "data structures and algorithms",
                                "database management"
                            ],
                            "have": [
                                "Python",
                                "scrum methodology"
                            ],
                            "match_percentage": "50"
                        }
                    }
                ]
            }
        }
        

        self.assertEqual(response.json, actual_response_body)

    # Get filtered roles for no filtered options passed
    def test_role_listing_filter_no_options_passed(self):
        request_body = {
            'category': [],
            'department': [],
            'match_percentage': []
        }

        response = self.client.post("/staff/filter_role_listings/1",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        actual_response_body = {
            "code": 404,
            "message": "No filter options were chosen."    
        }
        

        self.assertEqual(response.json, actual_response_body)

    # Get filtered roles no role listing found
    def test_role_listing_filter_none_found(self):
        request_body = {
            'category': [],
            'department': [],
            'match_percentage': ['81-100']
        }

        response = self.client.post("/staff/filter_role_listings/1",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        actual_response_body = {
            "code": 404,
            "message": "No role listings found for the given filter options."
        }
        

        self.assertEqual(response.json, actual_response_body)


if __name__ == '__main__':
    unittest.main()

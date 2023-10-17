import unittest
import datetime 
import sys
sys.path.append('../../backend/models')


from access_rights import AccessRights
from category import Category
from job_application import JobApplication
from login_details import LoginDetails
from role_listing import RoleListing
from role_skill import RoleSkill
from role import Role
from skills import Skill
from staff_skill import StaffSkill
from staff import Staff


class TestSBRP(unittest.TestCase):
    def test_access_rights(self):
        ar = AccessRights(access_right = 1, user_role = "staff")
        self.assertEqual(ar.json(),{'access_right': 1, 'user_role': 'staff'})

    def test_category(self):
        ar = Category(category = "IT",category_desc ="information systems")
        self.assertEqual(ar.json(),{'category': 'IT', 'category_desc': 'information systems'})

    def test_job_application(self):
        date_today = datetime.date.today()
        ar = JobApplication(staff_id = 1,listing_id =1, application_date=date_today)
        self.assertEqual(ar.json(),{'application_id': None, 'staff_id': 1, 'listing_id': 1, "application_date": date_today.strftime(date_today.strftime('%Y-%m-%d'))})

# Making sure the codes in it runs only if u run the file directly
if __name__ == "__main__":
    unittest.main()
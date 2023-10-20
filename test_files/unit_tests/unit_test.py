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
        ar = AccessRights(access_id = 1, access_control_name = "staff")
        self.assertEqual(ar.json(),{'access_id': 1, 'access_control_name': 'staff'})

    def test_category(self):
        category = Category(category = "IT",category_desc ="information systems")
        self.assertEqual(category.json(),{'category': 'IT', 'category_desc': 'information systems'})

    def test_job_application(self):
        date_today = datetime.date.today()
        ja = JobApplication(application_id= 1, staff_id = 1,listing_id =1, application_date=date_today)
        self.assertEqual(ja.json(),{'application_id': 1, 'staff_id': 1, 'listing_id': 1, "application_date": date_today.strftime(date_today.strftime('%Y-%m-%d'))})

    def test_login_details(self):
        ld = LoginDetails(staff_id = 1,staff_password ="john")
        self.assertEqual(ld.json(),{'staff_id': 1, 'staff_password': 'john'})

    def test_role_listing(self):
        date_today = datetime.date.today()
        rl = RoleListing(listing_id = 1, role_name = "IT", department = "information systems", category = "IT", deadline =date_today)
        self.assertEqual(rl.json(), {'listing_id': 1, 'role_name': 'IT', 'department': 'information systems', 'category': 'IT','deadline': date_today.strftime(date_today.strftime('%Y-%m-%d'))})

    def test_role_skill(self):
        rs = RoleSkill(role_name = "IT", skill_name = "python")
        self.assertEqual(rs.json(), {'role_name': 'IT', 'skill_name': 'python'})

    def test_role(self):
        role = Role(role_name = "IT", role_desc = "information systems")
        self.assertEqual(role.json(), {'role_name': 'IT', 'role_desc': 'information systems'})

    def test_skils(self):
        skill = Skill(skill_name = "python", skill_desc="programming")
        self.assertEqual(skill.json(), {'skill_name': 'python', 'skill_desc': 'programming'})
    
    def test_staff_skill(self):
        ss = StaffSkill(staff_id = 1, skill_name = "python")
        self.assertEqual(ss.json(), {'staff_id': 1, 'skill_name': 'python'})

    def test_staff(self):
        staff = Staff(staff_id = 1, staff_fname = "john", staff_lname = "tan", dept = "it", country="singapore", email="johntan@email.com", role=1) 
        self.assertEqual(staff.json(), {'staff_id': 1, 'staff_fname': 'john', 'country': 'singapore', 'staff_lname': 'tan', 'dept': 'it', 'email': 'johntan@email.com', "role": 1})

# Making sure the codes in it runs only if u run the file directly
if __name__ == "__main__":
    unittest.main()
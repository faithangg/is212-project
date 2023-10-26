from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class Login(unittest.TestCase):
    @classmethod
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        # Create a google chrome session
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        # Navigate to the application home page
        self.driver.get("http://localhost:8080")
    
    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()
        time.sleep(3)

    # HELPER FUNCTION: LOGIN AS HR
    def login(self):    
        # find the textbox to input the staff id
        self.staff_id = self.driver.find_element(By.ID, "staffId")
        self.staff_id.clear()
        self.staff_id.send_keys(140004)

        # find the textbox to input the password
        self.password = self.driver.find_element(By.ID, "password")
        self.password.clear()
        self.password.send_keys("mary")

        # find the button and click it
        self.driver.find_element(By.ID, "login").click()

    # TEST CASE: CREATE ROLE LISTING
    def test_create_role_listing(self):
        # Login as HR
        self.login()
        time.sleep(3)
        
        # Go to the manage role listing page
        self.driver.find_element(By.ID, "nav_bar_icon").click()
        text = self.driver.find_element(By.ID, "managed_nav").click()

        time.sleep(3)

        # Click on the crete role listing button
        self.driver.find_element(By.ID, "create_role_listing_btn").click()

        time.sleep(3)

        # Select the role
        role = self.driver.find_element(By.ID, "role")
        role.send_keys(Keys.RETURN)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[text() = "Developer"]').click()

        time.sleep(1)


        # Select the department
        dept = self.driver.find_element(By.ID, "department")
        dept.send_keys(Keys.RETURN)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[text() = "Sales"]').click()
        dept.send_keys(Keys.DOWN)
        dept.send_keys(Keys.RETURN)

        # Select the category
        dept = self.driver.find_element(By.ID, "category")
        dept.send_keys(Keys.RETURN)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[text() = "Information Technology"]').click()
        dept.send_keys(Keys.DOWN)
        dept.send_keys(Keys.RETURN)

        time.sleep(1)

        # Select the application deadline
        application_deadline = self.driver.find_element(By.ID, "application_deadline")
        application_deadline.send_keys("08/08/2024")

        time.sleep(1)

        # Click the create role button
        self.driver.find_element(By.ID, "create_role_btn").click()

        time.sleep(3)
        
        # Get the text of the success alert
        text = self.driver.find_element(By.ID, "success_alert").text

        # Check if the alert is correct
        self.assertIn("New role created successfully", text)

    # TEST CASE: UPDATE ROLE LISTING
    def test_update_role_listing(self):
        # Login as HR
        self.login()
        time.sleep(3)
        
        # Go to the manage role listing page
        self.driver.find_element(By.ID, "nav_bar_icon").click()
        text = self.driver.find_element(By.ID, "managed_nav").click()

        time.sleep(3)

        # Click the edit button for the first role listing
        self.driver.find_element(By.ID, "edit").click()
        time.sleep(3)

        # Change the deadline of the role listing
        application_deadline = self.driver.find_element(By.ID, "application_deadline")
        application_deadline.send_keys("10/08/2024")

        # Click the update button
        self.driver.find_element(By.ID, "update_btn").click()

        time.sleep(1)

        # Get the text of the success alert
        text = self.driver.find_element(By.ID, "updated_success_alert").text

        # Check if the alert is correct
        self.assertIn("Role updated successfully", text)

    # TEST CASE: ROLE APPLICANTS
    def test_role_applicants(self):
        # Login as HR
        self.login()
        time.sleep(3)

        # Go to the manage role listing page
        self.driver.find_element(By.ID, "nav_bar_icon").click()
        text = self.driver.find_element(By.ID, "managed_nav").click()

        time.sleep(3)

        # Click the view applicants button for the first role listing
        self.driver.find_element(By.ID, "view_applicants").click()
        time.sleep(3)

        # Get the role name
        text = self.driver.find_element(By.ID, "role_applicants_title").text

        # Check if its the correct role
        self.assertIn("Applicants for", text)
            
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
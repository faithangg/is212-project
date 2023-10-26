from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class Staff(unittest.TestCase):
    @classmethod
    # Called before every test case
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")  
        # Create a google chrome session
        self.driver = webdriver.Chrome(options=options)
        # Navigate to the application home page
        self.driver.get("http://localhost:8080")
    
    @classmethod
    # Called after every test case
    def tearDown(self):
        # close the browser window
        self.driver.quit()
        time.sleep(3)

    # HELPER FUNCTION: LOGIN AS STAFF
    def login(self):
        # find the textbox to input the staff id
        self.staff_id = self.driver.find_element(By.ID, "staffId")
        self.staff_id.clear()
        self.staff_id.send_keys(140002)

        # find the textbox to input the password
        self.password = self.driver.find_element(By.ID, "password")
        self.password.clear()
        self.password.send_keys("susan")

        # find the button and click it
        self.driver.find_element(By.ID, "login").click()

    # STAFF TEST CASE: BROWSE ROLE LISTING
    def test_browse_role_listing_staff(self):
        # Login
        self.login()
        time.sleep(2)

        # Search for senior engineer role
        search_bar = self.driver.find_element(By.ID, "search_bar")
        search_bar.clear()
        search_bar.send_keys("senior engineer")

        # Click search button
        self.driver.find_element(By.ID, "search_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Get the first role listing name
        text = self.driver.find_element(By.ID, "role_name").text

        # Check if role listing has the word legal in it
        self.assertIn("senior", text.lower())

    # STAFF TEST CASE: BROWSE ROLE LISTING NO RESULT
    def test_browse_role_listing_no_result(self):
        # Login
        self.login()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Search for a role that does not exist
        search_bar = self.driver.find_element(By.ID, "search_bar")
        search_bar.clear()
        search_bar.send_keys("cannot")

        # Click search button
        self.driver.find_element(By.ID, "search_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Get the info alert text
        text = self.driver.find_element(By.ID, "search_alert").text

        # Check if the its the correct alert
        self.assertIn("no role listings found", text.lower())

    # STAFF TEST CASE: BROWSE ROLE LISTING WITH SPECIAL CHARACTERS
    def test_browse_role_listing_special_characters(self):
        # Login
        self.login()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Search for a role that does not exist
        search_bar = self.driver.find_element(By.ID, "search_bar")
        search_bar.clear()
        search_bar.send_keys("%")

        # Click search button
        self.driver.find_element(By.ID, "search_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Get the info alert text
        text = self.driver.find_element(By.ID, "search_alert").text

        # Check if the its the correct alert
        self.assertIn("Invalid search query - No special characters", text)

    # STAFF TEST CASE: APPLY ROLE
    def test_apply_role(self):
        # Login
        self.login()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Open the first modal 
        self.driver.find_element(By.ID, "role_listing_card").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Click apply role button
        self.driver.find_element(By.ID, "apply_role").click()
        
        time.sleep(1)

        # Get the text of the success alert
        text = self.driver.find_element(By.ID, "apply_success_alert").text
        
        # Check if the alert is correct
        self.assertIn("You have successfully applied for the role", text)

    # STAFF TEST CASE: FILTER ROLE LISTING
    def test_filter_role_listing(self):
        # Login
        self.login()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Open filter modal
        time.sleep(5)

        # Click the filters (category, department, match percentage)
        self.driver.find_element(By.ID, "category_Consulting").click()

        self.driver.find_element(By.ID, "0-20").click()

        # Click apply filter button
        self.driver.find_element(By.ID, "apply_filter_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Get the department of the first role listing
        text = self.driver.find_element(By.ID, "listing_department").text

        # Check if the department is the one we selected in the filter
        self.assertIn("Consultancy", text)

    # STAFF TEST CASE: FILTER ROLE LISTING NO RESULT
    def test_filter_role_listing_no_result(self):
        # Login
        self.login()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Click the filters (department, category, match percentage)
        self.driver.find_element(By.ID, "category_Finance").click()
        self.driver.find_element(By.ID, "0-20").click()

        # Click apply filter button
        self.driver.find_element(By.ID, "apply_filter_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Get the alert text
        text = self.driver.find_element(By.ID, "filter_alert").text

        # Check if the alert is correct
        self.assertIn("No role listings found based on your input filters", text)

    # HR TEST CASE: CREATE ROLE LISTING
    def test_create_role_listing(self):
        # Login
        self.login()
        time.sleep(3)
        
        # Go to the manage role listing page
        text = self.driver.find_element(By.ID, "managed").click()

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

    # HR TEST CASE: CREATE THE SAME ROLE LISTING
    def test_create_same_role_listing(self):
        # Login
        self.login()
        time.sleep(3)
        
        # Go to the manage role listing page
        text = self.driver.find_element(By.ID, "managed").click()

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
        text = self.driver.find_element(By.ID, "error_alert").text

        # Check if the alert is correct
        self.assertIn("This role already exists. Please check your input and try again.", text)

    # HR TEST CASE: UPDATE ROLE LISTING
    def test_update_role_listing(self):
        # Login
        self.login()
        time.sleep(3)
        
        # Go to the manage role listing page
        text = self.driver.find_element(By.ID, "managed").click()

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

    # HR TEST CASE: ROLE APPLICANTS
    def test_role_applicants(self):
        # Login
        self.login()
        time.sleep(3)

        # Go to the manage role listing page
        text = self.driver.find_element(By.ID, "managed").click()

        time.sleep(3)

        # Click the view applicants button for the first role listing
        self.driver.find_element(By.ID, "view_applicants").click()
        time.sleep(3)

        # Get the role name
        text = self.driver.find_element(By.ID, "role_applicants_title").text

        # Check if its the correct role
        self.assertIn("Applicants for", text)

    # HR TEST CASE: FILTER AND SORT ROLE APPLICANTS
    def test_filter_sort_role_applicants(self):
        # Login
        self.login()
        time.sleep(3)

        # Go to the manage role listing page
        text = self.driver.find_element(By.ID, "managed").click()

        time.sleep(3)

        # Click the view applicants button for the first role listing
        self.driver.find_element(By.ID, "view_applicants").click()
        time.sleep(3)

        # Get the role name
        text = self.driver.find_element(By.ID, "role_applicants_title").text

        # Click the filters
        search_bar = self.driver.find_element(By.ID, "department_Sales").click()
        search_bar = self.driver.find_element(By.ID, "0-20").click()

        # Click apply filter button
        self.driver.find_element(By.ID, "apply_filter_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)
        text = self.driver.find_element(By.ID, "dept").text

        # Check if its the correct department
        self.assertIn("Sales", text)

    # HR TEST CASE: FILTER ROLE APPLICANTS NO RESULT
    def test_filter_sort_role_applicants(self):
        # Login
        self.login()
        time.sleep(3)

        # Go to the manage role listing page
        text = self.driver.find_element(By.ID, "managed").click()

        time.sleep(3)

        # Click the view applicants button for the first role listing
        self.driver.find_element(By.ID, "view_applicants").click()
        time.sleep(3)

        # Get the role name
        text = self.driver.find_element(By.ID, "role_applicants_title").text

        # Click the filters
        search_bar = self.driver.find_element(By.ID, "department_Sales").click()
        search_bar = self.driver.find_element(By.ID, "41-60").click()

        # Click apply filter button
        self.driver.find_element(By.ID, "apply_filter_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)
        text = self.driver.find_element(By.ID, "filter_alert").text

        # Check if its the correct department
        self.assertIn("No applicants found based on your input filters", text)

    # HR TEST CASE: BROWSE ROLE LISTING
    def test_hr_browse_role_listing_staff(self):
        # Login
        self.login()
        time.sleep(2)

        # Search for senior engineer role
        search_bar = self.driver.find_element(By.ID, "search_bar")
        search_bar.clear()
        search_bar.send_keys("senior engineer")

        # Click search button
        self.driver.find_element(By.ID, "search_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Get the first role listing name
        text = self.driver.find_element(By.ID, "role_name").text

        # Check if role listing has the word legal in it
        self.assertIn("senior", text.lower())

    # HR TEST CASE: BROWSE ROLE LISTING NO RESULTS
    def test_hr_browse_role_listing_no_result(self):
        # Login
        self.login()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Search for a role that does not exist
        search_bar = self.driver.find_element(By.ID, "search_bar")
        search_bar.clear()
        search_bar.send_keys("cannot")

        # Click search button
        self.driver.find_element(By.ID, "search_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Get the info alert text
        text = self.driver.find_element(By.ID, "search_alert").text

        # Check if the its the correct alert
        self.assertIn("no role listings found", text.lower())

    # HR TEST CASE: BROWSE ROLE LISTING WITH SPECIAL CHARACTERS
    def test_hr_browse_role_listing_special_characters(self):
        # Login
        self.login()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Search for a role that does not exist
        search_bar = self.driver.find_element(By.ID, "search_bar")
        search_bar.clear()
        search_bar.send_keys("%")

        # Click search button
        self.driver.find_element(By.ID, "search_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Get the info alert text
        text = self.driver.find_element(By.ID, "search_alert").text

        # Check if the its the correct alert
        self.assertIn("Invalid search query - No special characters", text)

    # TEST CASE: STAFF VIEW THEIR DETAILS
    def test_staff_profile(self):
        # Login
        self.login()
        time.sleep(3)

        # Go to the manage role listing page
        text = self.driver.find_element(By.ID, "profilepage").click()
        time.sleep(3)

        # Get the Staff ID
        text = self.driver.find_element(By.ID, "staff_id").text

        # Check if its the correct department
        self.assertIn("140002", text)

    # TEST CASE: STAFF VIEW ROLES THEY APPLY FOR
    def test_staff_applied_roles(self):
        # Login
        self.login()
        time.sleep(3)

        # Go to the manage role listing page
        text = self.driver.find_element(By.ID, "profilepage").click()
        time.sleep(3)

        # Get the Staff ID
        roles_applied = self.driver.find_elements(By.ID, "role_applied_card")

        # Get the number of roles applied 
        num_applied = len(roles_applied)

        # Check if the number of roles is either 2 / 3 (acc to the test data)
        self.assertTrue(num_applied == 2 or num_applied == 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
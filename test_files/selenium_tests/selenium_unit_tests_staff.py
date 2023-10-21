from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import unittest

class Staff(unittest.TestCase):
    @classmethod
    # Called before every test case
    def setUp(self):
        # Create a google chrome session
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
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

    # TEST CASE: BROWSE ROLE LISTING
    def test_browse_role_listing_staff(self):
        # Login as staff
        self.login()
        # Go to role listing page
        text = self.driver.find_element(By.ID, "role_listings").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Search for legal advisor role
        search_bar = self.driver.find_element(By.ID, "search_bar")
        search_bar.clear()
        search_bar.send_keys("legal advisor")

        # Click search button
        self.driver.find_element(By.ID, "search_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Get the first role listing name
        text = self.driver.find_element(By.ID, "role_name").text

        # Check if role listing has the word legal in it
        self.assertIn("legal", text.lower())

    # TEST CASE: BROWSE ROLE LISTING NO RESULT
    def test_browse_role_listing_no_result(self):
        # Login as staff
        self.login()

        # Go to role listing page
        text = self.driver.find_element(By.ID, "role_listings").click()

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

    # TEST CASE: APPLY ROLE
    def test_apply_role(self):
        # Login as staff
        self.login()

        # Go to role listing page
        text = self.driver.find_element(By.ID, "role_listings").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Open the first modal 
        self.driver.find_element(By.ID, "open_modal").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Click apply role button
        self.driver.find_element(By.ID, "apply_role").click()
        
        time.sleep(1)

        # Get the text of the success alert
        text = self.driver.find_element(By.ID, "apply_success_alert").text
        
        # Check if the alert is correct
        self.assertIn("You have successfully applied for the role", text)

    # TEST CASE: FILTER ROLE LISTING
    def test_filter_role_listing(self):
        # Login as staff
        self.login()

        # Go to role listing page
        text = self.driver.find_element(By.ID, "role_listings").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Click the filters (category, department, match percentage)
        self.driver.find_element(By.ID, "category_Information Technology").click()
        self.driver.find_element(By.ID, "department_IT").click()
        self.driver.find_element(By.ID, "41-60").click()

        # Click apply filter button
        self.driver.find_element(By.ID, "apply_filter_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Get the department of the first role listing
        text = self.driver.find_element(By.ID, "listing_department").text

        # Check if the department is the one we selected in the filter
        self.assertIn("IT", text)

    # TEST CASE: FILTER ROLE LISTING NO RESULT
    def test_filter_role_listing_no_result(self):
        # Login as staff
        self.login()

        # Go to role listing page
        text = self.driver.find_element(By.ID, "role_listings").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Click the filters (department, category, match percentage)
        self.driver.find_element(By.ID, "category_Finance").click()
        self.driver.find_element(By.ID, "department_Finance").click()
        self.driver.find_element(By.ID, "0-20").click()

        # Click apply filter button
        self.driver.find_element(By.ID, "apply_filter_btn").click()

        # Wait for 3 seconds (for the page to load)
        time.sleep(3)

        # Get the alert text
        text = self.driver.find_element(By.ID, "filter_alert").text

        # Check if the alert is correct
        self.assertIn("No role listings found based on your input filters", text)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)
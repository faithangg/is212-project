import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080")
staff_id = driver.find_element(By.ID, "staffId")
staff_id.clear()
staff_id.send_keys(160332)

password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("somchai")

driver.find_element(By.ID, "login").click()

text = driver.find_element(By.ID, "managed").click()

time.sleep(3)

create_btn = driver.find_element(By.ID, "create_role_listing_btn").click()

time.sleep(3)

# Select the role
role = driver.find_element(By.ID, "role")
role.send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element(By.XPATH, '//*[text() = "Software Engineer"]').click()

time.sleep(1)


# Select the department
dept = driver.find_element(By.ID, "department")
dept.send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element(By.XPATH, '//*[text() = "IT"]').click()
dept.send_keys(Keys.DOWN)
dept.send_keys(Keys.RETURN)

# Select the category
dept = driver.find_element(By.ID, "category")
dept.send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element(By.XPATH, '//*[text() = "Information Technology"]').click()
dept.send_keys(Keys.DOWN)
dept.send_keys(Keys.RETURN)

time.sleep(1)

# Select the application deadline
application_deadline = driver.find_element(By.ID, "application_deadline")
application_deadline.send_keys("08/08/2024")

time.sleep(1)

driver.find_element(By.ID, "create_role_btn").click()

time.sleep(3)

try: 
    text = driver.find_element(By.ID, "success_alert").text
    assert "New role created successfully" in text
except:
    text = driver.find_element(By.ID, "error_alert").text
    assert "This role already exists. Please check your input and try again." in text

print("TEST PASSED : Create Role Listing")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

# Login first
driver.get("http://localhost:8080")

# Enter staff id
staff_id = driver.find_element(By.ID, "staffId")
staff_id.clear()
staff_id.send_keys(140002)

# Enter password
password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("susan")

# Click login button
driver.find_element(By.ID, "login").click()

# Go to role listing page
text = driver.find_element(By.ID, "role_listings").click()

# Wait for 3 seconds (for the page to load)
time.sleep(3)

# Open the first modal 
element = driver.find_element(By.ID, "open_modal").click()

# Wait for 3 seconds (for the page to load)
time.sleep(3)

text = driver.find_element(By.ID, "apply_role").get_attribute("id")

assert "apply_role" in text

print("TEST PASSED : Role Listing Details Staff")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
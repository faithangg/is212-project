import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest

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

time.sleep(3)

# Go to managed role listing page
text = driver.find_element(By.ID, "managed").click()
time.sleep(3)

# Open the first modal
element = driver.find_element(By.ID, "view_applicants")
element.click()
time.sleep(3)

try:
    # Sort applicants by match percentage
    sort = driver.find_element(By.ID, "sort_dropdown")
    sort.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[text() = "Match Percentage (High to Low)"]').click()
    time.sleep(1)
    # Check if the email is displayed
    text = driver.find_element(By.ID, "email").text
    assert "Email:" in text
    print("TEST PASSED : Sort Role Applicants.")
except:
    text = driver.find_element(By.ID, "no_applicants_alert").text
    assert "No applicants for this role." in text
    print("TEST FAILED : Couldn't sort applicants as there are none.")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
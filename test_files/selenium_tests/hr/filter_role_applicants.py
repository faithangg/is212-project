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
staff_id.send_keys(160332)

# Enter password
password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("somchai")

# Click login button
driver.find_element(By.ID, "login").click()
time.sleep(3)

# Go to manage role listing page
text = driver.find_element(By.ID, "managed").click()
time.sleep(3)

# Open the first modal
element = driver.find_element(By.ID, "view_applicants")
element.click()
time.sleep(3)

try:
    # Click the filters
    search_bar = driver.find_element(By.ID, "department_HR").click()
    search_bar = driver.find_element(By.ID, "0-20").click()

    # Click apply filter button
    driver.find_element(By.ID, "apply_filter_btn").click()

    # Wait for 3 seconds (for the page to load)
    time.sleep(3)
    text = driver.find_element(By.ID, "dept").text

    # Check if the dept is correct
    assert "HR" in text
    print("TEST PASSED : FILTER APPLICANTS.")
except:
    text = driver.find_element(By.ID, "no_applicants_alert").text
    assert "No applicants for this role." in text
    print("TEST FAILED : Couldn't filter applicants as there are none.")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
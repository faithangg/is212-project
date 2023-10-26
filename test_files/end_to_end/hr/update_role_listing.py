import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080")
staff_id = driver.find_element(By.ID, "staffId")
staff_id.clear()
staff_id.send_keys(140002)

password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("susan")

driver.find_element(By.ID, "login").click()

text = driver.find_element(By.ID, "managed").click()

time.sleep(3)

element = driver.find_element(By.ID, "edit")
element.click()
time.sleep(3)

application_deadline = driver.find_element(By.ID, "application_deadline")
application_deadline.send_keys("08/08/2024")
driver.find_element(By.ID, "update_btn").click()

time.sleep(2)

text = driver.find_element(By.ID, "updated_success_alert").text

assert "Role updated successfully" in text
print("TEST PASSED : UPDATE ROLE LISTING.")
print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
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
staff_id.send_keys(160332)

password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("somchai")

driver.find_element(By.ID, "login").click()

time.sleep(3)

text = driver.find_element(By.ID, "managed").click()

time.sleep(3)

element = driver.find_element(By.ID, "view_applicants")
element.click()
time.sleep(3)

try:
    text = driver.find_element(By.ID, "role_applicants_title").text
    assert "Applicants for " in text
    print("TEST PASSED : View Role Applicants.")
except:
    text = driver.find_element(By.ID, "no_applicants_alert").text
    assert "No applicants for this role." in text
    print("TEST PASSED : View Role Applicants.")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
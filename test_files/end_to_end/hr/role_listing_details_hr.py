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


element = driver.find_element(By.ID, "open_modal")
time.sleep(3)

element.click()

text = driver.find_element(By.ID, "edit").get_attribute("class")

print("text", text)

assert "mdi-pencil" in text

print("TEST PASSED : Role Listing Details HR")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
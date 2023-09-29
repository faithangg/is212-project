from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080/manageRolesPage")


element = driver.find_element(By.ID, "open_modal")

element.click()

text = driver.find_element(By.ID, "edit").get_attribute("class")

print("text", text)

assert "mdi-pencil" in text

print("TEST PASSED : Role Listing Details HR")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
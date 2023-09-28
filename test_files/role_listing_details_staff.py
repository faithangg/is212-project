from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080/viewRolesPage")


element = driver.find_element(By.ID, "open_modal")

element.click()

text = driver.find_element(By.ID, "apply_role").get_attribute("id")

assert "apply_role" in text

print("TEST PASSED : Role Listing Details Staff")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080/viewRolesPage")


driver.find_element(By.ID, "open_modal").click()

driver.find_element(By.ID, "apply_role").click

text = driver.find_element(By.ID, "apply_alerts").get_attribute("id")

assert "apply_alerts" in text

print("TEST PASSED : Apply Role")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080/viewRolesPage")


element = driver.find_element(By.ID, "search_bar")
element.clear()
element.send_keys("software")

driver.find_element(By.ID, "search_btn").click()

text = driver.find_element(By.ID, "role_name").text

assert "software" in text.lower()

print("TEST PASSED : Role Listing Details Staff")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
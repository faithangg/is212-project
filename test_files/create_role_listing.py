import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080")
staff_id = driver.find_element(By.ID, "staffId")
staff_id.clear()
staff_id.send_keys(2)

password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("jane")

driver.find_element(By.ID, "login").click()

text = driver.find_element(By.ID, "managed").click()

time.sleep(3)

create_btn = driver.find_element(By.ID, "create_role_listing_btn").click()

time.sleep(3)

# Select the role
role = driver.find_element(By.ID, "role")
# role.select_by_visible_text("Software Engineer")
role.send_keys(Keys.DOWN)
role.send_keys(Keys.RETURN)

time.sleep(3)

print(role.text)


time.sleep(1)


print("here")
# # Select the department
# dept = Select(driver.find_element(By.ID, "department"))
# dept.select_by_visible_text("IT")

dept = driver.find_element(By.ID, "department").click()
# role.select_by_visible_text("Software Engineer")
dept.send_keys(Keys.DOWN)
dept.send_keys(Keys.RETURN)

# # Select the category
# category = Select(driver.find_element(By.ID, "category"))
# category.select_by_visible_text("Engineering")

# # Select the application deadline
# category = driver.find_element(By.ID, "application_deadline")
# category.send_keys("08/08/2024")

# driver.find_element(By.ID, "create_role_btn").click()

# text = driver.find_element(By.ID, "alert").text

# assert "New role created successfully" in text

# print("TEST PASSED : Create Role Listing")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080")

# find the textbox to input the staff id
staff_id = driver.find_element(By.ID, "staffId")
staff_id.clear()
staff_id.send_keys(140002)

# find the textbox to input the password
password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("susan")

# find the button and click it
driver.find_element(By.ID, "login").click()

# check if it redirects to the correct page (if u see manage role listing in the navbar its wrong)
text = driver.find_element(By.ID, "managed").text
try:  
    assert "MANAGE ROLE LISTINGS" in text
    print("TEST FAILED : LOGIN UNSUCCESSFUL")
    
except:
    assert "VIEW ROLE LISTINGS" in text
    print("TEST PASSED : LOGIN SUCCESSFUL")


print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
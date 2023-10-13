from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080")
staff_id = driver.find_element(By.ID, "staffId")
staff_id.clear()
staff_id.send_keys(2)

password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("john")

driver.find_element(By.ID, "login").click()


try:
    text = driver.find_element(By.ID, "managed").text
    assert "MANAGE ROLE LISTINGS" in text

    print("TEST PASSED : LOGIN FAILED")
    
except:
    text = driver.find_element(By.ID, "role_listings").text
    assert "VIEW ROLE LISTINGS" in text

    print("TEST PASSED : LOGIN SUCCESSFUL")


print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()
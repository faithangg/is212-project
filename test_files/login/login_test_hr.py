import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def hr_login():
    # create webdriver object
    driver = webdriver.Chrome()
    driver.maximize_window()

    # get url
    driver.get("http://localhost:8080")

    # find the textbox to input the staff id
    staff_id = driver.find_element(By.ID, "staffId")
    staff_id.clear()
    staff_id.send_keys(2)

    # find the textbox to input the password
    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys("jane")

    # find the button and click it
    driver.find_element(By.ID, "login").click()

    time.sleep(2)

    # check if it redirects to the correct page (if u see manage role listing in the navbar its correct)
    text = driver.find_element(By.ID, "managed").text

    try:
        assert "MANAGE ROLE LISTINGS" in text
        driver.quit()
        return "TEST PASSED : LOGIN SUCCESSFUL"
    except:
        driver.quit()
        return "TEST FAILED : LOGIN UNSUCCESSFUL"
    
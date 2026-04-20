import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


def test_login_xpath_absolute(selenium):
    selenium.get("https://kodilla.com/pl/test/login")
    wait=WebDriverWait(selenium,60)

    #email_field = selenium.find_element(By.XPATH, "/html/body/section/form/div[1]/input")
    email_field = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/section/form/div[1]/input"))
    )
    email_field.clear()
    email_field.send_keys("test@kodilla.com")

    password_field = selenium.find_element(By.XPATH, "/html/body/section/form/div[2]/input")
    password_field.clear()
    password_field.send_keys("kodilla123")
    login_button = selenium.find_element(By.XPATH, "/html/body/section/form/button")
    login_button.click()
    
    alert = WebDriverWait(selenium, 10).until(EC.alert_is_present())
    assert alert.text == "Jesteś teraz zalogowany!"


def test_select_xpath_position(selenium):
    selenium.get("https://kodilla.com/pl/test/form/")
    wait=WebDriverWait(selenium,60)

    year_combo = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//select[3]"))
    )
    Select(year_combo).select_by_index(5)

    time.sleep(3)
    selenium.quit()

def test_select_xpath_relative(selenium):
    selenium.get("https://kodilla.com/pl/test/form/")
    wait=WebDriverWait(selenium,60)

    year_combo = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id = 'birthday_wrapper']/select[3]"))
    )
    Select(year_combo).select_by_index(5)

    time.sleep(3)
    selenium.quit()
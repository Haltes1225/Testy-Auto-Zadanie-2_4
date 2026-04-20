from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def assert_amount(driver, search_phrase, amount):
    driver.get("https://kodilla.com/pl/test/store")
    wait=WebDriverWait(driver,60)

    search_bar = wait.until(
        EC.element_to_be_clickable((By.ID, "searchField"))
    )
    search_bar.clear()
    search_bar.send_keys(search_phrase)

    wait.until(
        EC.presence_of_element_located((By.XPATH, "//section/div[@id = 'elements-wrapper']"))
    )
    elements = driver.find_elements(By.XPATH, "//section/div[@id = 'elements-wrapper']/div[@class = 'element']")
    
    assert len(elements) == amount

def test_store(selenium):
    assert_amount(selenium, "Laptop", 3)
    assert_amount(selenium, "NoteBook", 2)
    assert_amount(selenium, "Gaming", 1)
    assert_amount(selenium, "Specyfikacja", 6)
    assert_amount(selenium, "Błyszcząca", 2)
    assert_amount(selenium, "Matowa", 4)
    assert_amount(selenium, "Alamakota", 0)



    
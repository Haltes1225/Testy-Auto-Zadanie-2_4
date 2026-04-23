from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def assert_amount(driver, search_phrase, amount):

    phrase_type = type(search_phrase)
    if not phrase_type is str:
        raise TypeError(f"amount must be str type, is {phrase_type}")

    amount_type = type(amount)
    if not amount_type is int:
        raise TypeError(f"amount must be int type, is {amount_type}")
    
    if not amount >= 0:
        raise ValueError("amount must be a non negative integer")
    
    wait=WebDriverWait(driver,10)

    search_bar = wait.until(
        EC.element_to_be_clickable((By.ID, "searchField"))
    )
    search_bar.clear()
    search_bar.send_keys(search_phrase)

    wait.until(
        lambda d: len(d.find_elements(By.XPATH, "//section/div[@id = 'elements-wrapper']/div[@class = 'element']")) == amount
    )
    elements = driver.find_elements(By.XPATH, "//section/div[@id = 'elements-wrapper']/div[@class = 'element']")

    assert len(elements) == amount

def test_store(selenium):
    selenium.get("https://kodilla.com/pl/test/store")
    assert_amount(selenium, "Laptop", 3)
    assert_amount(selenium, "NoteBook", 2)
    assert_amount(selenium, "Gaming", 1)
    assert_amount(selenium, "Specyfikacja", 6)
    assert_amount(selenium, "Błyszcząca", 2)
    assert_amount(selenium, "Matowa", 4)
    assert_amount(selenium, "Alamakota", 0)
    assert_amount(selenium, "14", 1)
    assert_amount(selenium, "+", 0)
    #assert_amount(selenium, 45, 32)
    #assert_amount(selenium, "+", "9")
    #assert_amount(selenium, "+", -1)



    
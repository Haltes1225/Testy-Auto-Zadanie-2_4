from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

def print_products_css(driver, search_phrase):

    phrase_type = type(search_phrase)
    if not phrase_type is str:
        raise TypeError(f"amount must be str type, is {phrase_type}")
    
    wait=WebDriverWait(driver,5)

    search_bar = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchField"))
    )
    search_bar.clear()
    search_bar.send_keys(search_phrase)

    try:
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#elements-wrapper > .element"))
        )
        elements = driver.find_elements(By.CSS_SELECTOR, "#elements-wrapper > .element")

        print("\n")
        for element in elements:
            print(element.text)
            print("\n")
    except TimeoutException:
        print("No search results to print")



def test_store_css(selenium):
    selenium.get("https://kodilla.com/pl/test/store")
    print_products_css(selenium, "Laptop")
    #print_products_css(selenium, "NoteBook")
    #print_products_css(selenium, "Gaming")
    #print_products_css(selenium, "Specyfikacja")
    #print_products_css(selenium, "Błyszcząca")
    #print_products_css(selenium, "Matowa")
    #print_products_css(selenium, "Alamakota")


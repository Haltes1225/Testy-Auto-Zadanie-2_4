import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

def highlight(element, effect_time, color, border):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)

def test_store(selenium):
    selenium.get("https://kodilla.com/pl/test/store")
    wait=WebDriverWait(selenium,60)

    search_bar = wait.until(
        EC.element_to_be_clickable((By.ID, "searchField"))
    )
    search_bar.clear()
    search_bar.send_keys("Laptop")
    time.sleep(3)

    wait.until(
        EC.presence_of_element_located((By.XPATH, "//section/div[@id = 'elements-wrapper']/div[@class = 'element']"))
    )
    elements = selenium.find_elements(By.XPATH, "//section/div[@id = 'elements-wrapper']/div[@class = 'element']")
    
    assert len(elements) == 3



    
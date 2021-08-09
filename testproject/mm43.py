from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/mm43.html")

    input_email = driver.find_element_by_id("email")
    submit_button = driver.find_element_by_id("submit")
    error_block = driver.find_element_by_xpath("//form[@onsubmit='return false']")


    def solution(a, b):
        input_email.clear()
        input_email.send_keys(a)
        submit_button.click()
        assert driver.find_element_by_class_name("validation-error").text == b  # used only once
        time.sleep(0.5)


    # TC_01
    input_email.send_keys("teszt@elek.hu")
    submit_button.click()
    assert len(error_block.get_attribute("class")) == 0  # because before any error, there's no class attribute here
    time.sleep(0.5)

    # TC_02
    solution("teszt@", "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.")

    # TC_03
    solution("", "Kérjük, töltse ki ezt a mezőt.")

finally:
    driver.close()

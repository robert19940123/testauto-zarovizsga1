from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/x234.html")

    a = driver.find_element_by_id("a")
    b = driver.find_element_by_id("b")


    def solution(one, two, three):
        a.clear()
        b.clear()
        a.send_keys(one)
        b.send_keys(two)
        driver.find_element_by_id("submit").click()  # used only once
        assert driver.find_element_by_id("result").text == three  # used only once
        time.sleep(1.0)


    # TC_01
    solution("99", "12", "222")

    # TC_02
    solution("kiskutya", "12", "NaN")

    # TC_03
    solution("", "", "NaN")

finally:
    driver.close()

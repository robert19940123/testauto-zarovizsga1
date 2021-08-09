from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html")

    # TC
    for _ in range(10):  # because each refresh changes the numbers etc.
        first = int(driver.find_element_by_id("num1").text)
        op = driver.find_element_by_id("op").text
        second = int(driver.find_element_by_id("num2").text)
        driver.find_element_by_id("submit").click()  # used only once
        result = int(driver.find_element_by_id("result").text)
        if op == "-":
            assert (first - second) == result
        if op == "*":
            assert (first * second) == result
        if op == "+":
            assert (first + second) == result
        driver.refresh()
        time.sleep(0.5)

finally:
    driver.close()

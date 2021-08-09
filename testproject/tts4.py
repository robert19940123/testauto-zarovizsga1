from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/tts4.html")

    # TC
    for _ in range(100):
        driver.find_element_by_id("submit").click()  # used only once
    time.sleep(1.0)

    head = []
    all_results = driver.find_elements_by_xpath("//li")
    for result in all_results:
        if result.text == "fej":
            head.append(result)

    assert len(head) >= 30

finally:
    driver.close()

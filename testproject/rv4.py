from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")

    # TC
    for _ in range(5):  # because each refresh changes the list (at least the order)
        input_field = driver.find_element_by_id("missingCity")
        city_list = driver.find_element_by_id("cites").text.split(", ")
        number = 0
        for x in range(len(city_list)):
            input_field.send_keys(city_list[number][1:-1])
            driver.find_element_by_id("submit").click()  # only used once
            number += 1
            result = driver.find_element_by_id("result").text
            if result != "Nem találtad el.":
                assert result == "Eltaláltad."
                time.sleep(0.5)
                break
            else:
                input_field.clear()
        driver.refresh()
        time.sleep(0.5)

finally:
    driver.close()

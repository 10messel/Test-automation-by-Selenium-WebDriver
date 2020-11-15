import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    x_input = browser.find_element_by_id("answer")
    x_value = browser.find_element_by_id("input_value").text
    browser.execute_script("window.scrollBy(0, 150);")
    x_input.send_keys(calc(x_value))
    time.sleep(1)

    browser.find_element_by_id("robotCheckbox").click()
    time.sleep(1)
    browser.find_element_by_id("robotsRule").click()
    time.sleep(1)

    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()

import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    chest = browser.find_element_by_id("treasure")
    x_value = chest.get_attribute("valuex")
    x_input = browser.find_element_by_id("answer").send_keys(calc(x_value))
    time.sleep(1)

    option1 = browser.find_element_by_id("robotCheckbox").click()
    time.sleep(1)
    option2 = browser.find_element_by_id("robotsRule").click()
    time.sleep(1)

    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()

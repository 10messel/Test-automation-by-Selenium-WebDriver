import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = browser.find_element_by_xpath('//div/h5[text()="$100"]')
    button1 = browser.find_element_by_id("book").click()
    time.sleep(1)

    x_value = browser.find_element_by_id("input_value").text
    x_input = browser.find_element_by_id("answer")
    x_input.send_keys(calc(x_value))
    time.sleep(1)

    button2 = browser.find_element_by_id("solve").click()

finally:
    time.sleep(5)
    browser.quit()

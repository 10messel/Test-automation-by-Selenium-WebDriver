import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button1 = browser.find_element_by_xpath('//div/button[text()="I want to go on a magical journey!"]').click()
    time.sleep(1)

    #    fir_window = browser.window_handles[0]
    sec_window = browser.window_handles[1]
    browser.switch_to.window(sec_window)

    x_value = browser.find_element_by_id("input_value").text
    x_input = browser.find_element_by_id("answer")
    x_input.send_keys(calc(x_value))

    button2 = browser.find_element_by_xpath('//div/button[text()="Submit"]').click()

finally:
    time.sleep(5)
    browser.quit()

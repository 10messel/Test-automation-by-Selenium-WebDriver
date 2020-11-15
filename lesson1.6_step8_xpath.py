import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    elements = browser.find_elements_by_tag_name("input")
    for i in elements:
        i.send_keys("My text")
        time.sleep(1)

    button = browser.find_element_by_xpath('//div/button[text()="Submit"]')
    button.click()

finally:
    time.sleep(5)
    browser.quit()

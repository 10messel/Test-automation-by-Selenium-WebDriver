import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    select_node = Select(browser.find_element_by_tag_name("select"))
    select_node.select_by_value(f"{int(num1) + int(num2)}")

    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()

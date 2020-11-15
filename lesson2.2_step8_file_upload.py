import os
import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    elements = browser.find_elements_by_class_name("form-control")
    values = ["Ivan", "Ivanov", "ivan.ivanov@gmail.com"]
    for i, j in enumerate(elements):
        j.send_keys(values[i])
        time.sleep(1)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Testfile.txt')
    select_file = browser.find_element_by_id("file")
    select_file.send_keys(file_path)
    time.sleep(1)

    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()

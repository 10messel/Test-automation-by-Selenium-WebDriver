import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    elements = browser.find_elements_by_css_selector("input[required]")
    values = ['Ivan', 'Ivanov', 'ivan.ivanov@gmail.com']
    for i, j in enumerate(elements):
        j.send_keys(values[i])
        time.sleep(1)

    button = browser.find_element_by_class_name("btn")
    button.click()
    time.sleep(5)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()

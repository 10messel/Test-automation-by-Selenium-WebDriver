import time
from selenium import webdriver


def test_registration_1():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        browser.get("http://suninjuly.github.io/registration1.html")

        required_elements = browser.find_elements_by_css_selector("input[required]")
        required_values = ['Ivan', 'Ivanov', 'ivan.ivanov@gmail.com']
        for i, j in enumerate(required_elements):
            j.send_keys(required_values[i])
            time.sleep(1)

        unrequired_elements = browser.find_elements_by_css_selector(".second_block div .form-control")
        unrequired_values = ['0123456789', 'Example street']
        for i, j in enumerate(unrequired_elements):
            j.send_keys(unrequired_values[i])
            time.sleep(1)

        browser.find_element_by_class_name("btn").click()

        welcome_text = "Congratulations! You have successfully registered!"
        welcome_text_elt = browser.find_element_by_tag_name("h1").text
        assert welcome_text == welcome_text_elt, "Error message"

    finally:
        time.sleep(5)
        browser.quit()


def test_registration_2():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        browser.get("http://suninjuly.github.io/registration2.html")

        required_elements = browser.find_elements_by_css_selector("input[required]")
        required_values = ['Ivan', 'ivan.ivanov@gmail.com']
        for i, j in enumerate(required_elements):
            j.send_keys(required_values[i])
            time.sleep(1)

        unrequired_elements = browser.find_elements_by_css_selector(".second_block div .form-control")
        unrequired_values = ['0123456789', 'Example street']
        for i, j in enumerate(unrequired_elements):
            j.send_keys(unrequired_values[i])
            time.sleep(1)

        browser.find_element_by_class_name("btn").click()

        welcome_text = "Congratulations! You have successfully registered!"
        welcome_text_elt = browser.find_element_by_tag_name("h1").text
        assert welcome_text == welcome_text_elt, "Error message"

    finally:
        time.sleep(5)
        browser.quit()

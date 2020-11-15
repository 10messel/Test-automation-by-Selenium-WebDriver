import time
import math
import pytest
from selenium import webdriver

message = ""


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_should_open_links_and_send_keys(browser, number):
    global message
    answer = str(math.log(int(time.time())))
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    time.sleep(3)
    input_value = browser.find_element_by_css_selector("div textarea")
    input_value.send_keys(answer)
    submit_button = browser.find_element_by_css_selector(".submit-submission")
    submit_button.click()
    feedback = "Correct!"
    feedback_elt = browser.find_element_by_css_selector(".smart-hints__hint").text
    if feedback != feedback_elt:
        message = message + f"{feedback_elt}"
    print(f"{message}")
    assert feedback == feedback_elt, f"expected '{feedback}', got '{feedback_elt}'"

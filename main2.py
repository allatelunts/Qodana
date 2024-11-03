from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_by_id(driver):
    data = 'Kim'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_element = driver.find_element(By.ID, 'id_text_string')
    input_element.send_keys(data)
    input_element.send_keys(Keys.ENTER)
    result = driver.find_element(By.ID, 'result-text')
    assert data == result.text


def test_by_class_name(driver):
    data = 'zina'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_element = driver.find_element(By.CLASS_NAME, 'form-control')
    input_element.send_keys(data)
    input_element.send_keys(Keys.ENTER)
    result = driver.find_element(By.CLASS_NAME, 'result-text')
    assert data == result.text


def test_by_tag_name(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    heading1 = driver.find_element(By.TAG_NAME, 'h1')
    assert heading1.text == 'Input field'


def test_css_selector(driver):
    data = 'zina'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    # input_element = driver.find_element(By.CSS_SELECTOR, '.form-control')
    input_element = driver.find_element(By.CSS_SELECTOR, "[placeholder='Submit me']")
    placeholder = input_element.get_attribute('placeholder')
    input_element.send_keys(data)
    input_element.send_keys(Keys.ENTER)
    assert placeholder == 'Submit me'
    assert data == driver.find_element(By.CSS_SELECTOR, '#result-text').text


def test_link(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    # contact_link = driver.find_element(By.LINK_TEXT, value='Contact')
    contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Contact')
    contact_link.click()
    # assert driver.find_element(By.TAG_NAME, 'h1').text == 'Contact us'
    assert driver.find_element(By.CSS_SELECTOR, 'h1').text == 'Contact us'



def test_xpath(driver):
    driver.get'https://www.qa-practice.com/elements/input/simple'
    input_element = driver.find_element(By.XPATH, '//*[@placeholder="Submit me"]')
    input_element.send_keys('hello')
    input_element.send_keys(Keys.ENTER)
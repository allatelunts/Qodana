from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_clear(driver):
    data = 'loreta'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_element = driver.find_element(By.NAME, 'text_string')
    input_element.send_keys(data)
    sleep(2)
    # input_element.clear()
    input_element_value = input_element.get_attribute('value')
    for _ in range(len(input_element_value)):
        input_element.send_keys(Keys.BACK_SPACE)
    assert input_element.get_attribute('value') == ''



def test_select(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    select = driver.find_element(By.ID, 'id_select_state')
    button = driver.find_element(By.ID, 'submit-id-submit')
    print(button.is_enabled())
    dropdown = Select(select)
    dropdown.select_by_value('enabled')
    print(button.is_enabled())



def test_add_cart(driver):
    driver.get('https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html')
    size = driver.find_element(By.ID, 'option-label-size-143-item-166')
    color = driver.find_element(By.ID, 'option-label-color-93-item-49')
    button = driver.find_element(By.ID, 'product-addtocart-button')
    size.click()
    color.click()
    button.click()
    wait = WebDriverWait(driver, 5)
    wait.until_not(
        EC.text_to_be_present_in_element_attribute(
            (By.CSS_SELECTOR, '.counter.qty'),
            'class',
            'loading'
        )
    )
    counter = driver.find_element(By.CSS_SELECTOR, '.counter-number')
    print("========================================", counter.text)


def test_product_title(driver):
    driver.get('https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html')
    products = driver.find_elements(By.CLASS_NAME, 'product-item-link')
    print(products[0].text)
    print(products[-1].text)
    for product in products:
        print(product.text)


def test_product_price(driver):
    driver.get('https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html')
    prices = driver.find_elements(By.CLASS_NAME, 'price')
    for price in prices:
        print(price.text)

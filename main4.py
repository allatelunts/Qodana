from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_new_tab(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    tabs = driver.window_handles # [123123791897, 4809580958]
    driver.switch_to.window(tabs[1])
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == 'I am a new page in a new tab'
    driver.close()
    driver.switch_to.window(tabs[0])


def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon').click()
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, 'Iframe').click()


def test_alert(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    alert = Alert(driver)
    sleep(3)
    alert.accept()
    sleep(3)


def test_drag_and_drop(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    elem1 = driver.find_element(By.ID, 'rect-droppable')
    elem2 = driver.find_element(By.ID, 'rect-draggable')
    ActionChains(driver).drag_and_drop(elem2, elem1).perform()
    actions = ActionChains(driver)
    actions.click_and_hold(elem2)
    actions.move_to_element(elem1)
    actions.perform()
    sleep(3)
    result = driver.find_element(By.ID, 'text-droppable')
    assert result.text == 'Dropped!'


def test_checkbox(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    checkbox.click()
    submit = driver.find_element(By.ID, 'submit-id-submit')
    submit.click()
    sleep(3)
    assert driver.find_element(By.ID, 'result-text').text == 'select me or not'


def test_new_tab_2(driver):
    driver.get('https://www.qa-practice.com/')
    homepage = driver.find_element(By.LINK_TEXT, 'Homepage')
    ActionChains(driver).key_down(Keys.CONTROL).click(homepage).key_up(Keys.CONTROL).perform()
    sleep(3)


def test_jackets(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    women = driver.find_element(By.ID, 'ui-id-4')
    tops = driver.find_element(By.ID, 'ui-id-9')
    jackets = driver.find_element(By.ID, 'ui-id-11')
    # ActionChains(driver).move_to_element(women).move_to_element(tops).click(jackets).perform()
    actions = ActionChains(driver)
    actions.move_to_element(women)
    actions.move_to_element(tops)
    actions.click(jackets)
    actions.perform()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Jackets'
    sleep(3)
    
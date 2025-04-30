from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest
from pages.main_page import MainPageYandexScooter
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Firefox(options=options)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPageYandexScooter(driver)

@pytest.fixture
def element(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

@pytest.fixture
def wait(driver):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.
                                                                   DROP_DOWN_LIST_IMPORTANT_QUESTIONS_8))
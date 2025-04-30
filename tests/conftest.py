from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest
from url import main_site


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Firefox(options=options)
    driver.get(main_site)
    yield driver
    driver.quit()

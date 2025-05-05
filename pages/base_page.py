import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ждём видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Получаем url сайта")
    def switch_and_get_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))
        current_url = self.driver.current_url
        return current_url

    @allure.step("Кликаем на элемент")
    def click_for_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()
        return element

    @allure.step("Кликаем на элемент")
    def click_for_element_with_scripts(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)
        return element

    @allure.step("Вводим текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)
        return element

    @allure.step("Получаем текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Скроллим до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

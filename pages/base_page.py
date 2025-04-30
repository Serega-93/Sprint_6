import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ждём видимости элемента")
    def wait_for_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Кликаем на элемент")
    def click_for_element(self, locator, timeout=5):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Вводим текст в поле ввода")
    def send_keys_to_input(self, keys, locator, timeout=5):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получаем текст элемента")
    def get_text_on_element(self, locator, timeout=5):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Скроллим до элемента")
    def scroll_to_element(self, locator, timeout=5):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Скроллим в конец страницы")
    def scroll_to_end_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
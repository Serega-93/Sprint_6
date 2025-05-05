import allure
from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
from url import yandex_logo_site


class HeaderPage(BasePage):

    @allure.step("Кликаем по логотипу Яндекс")
    def click_on_logo_yandex(self):
        self.click_for_element(HeaderPageLocators.LOGO_YANDEX)
        return self.switch_and_get_url(yandex_logo_site)

    @allure.step("Кликаем по логотипу Самокат")
    def click_on_logo_scooter(self):
        self.click_for_element(HeaderPageLocators.LOGO_SCOOTER)




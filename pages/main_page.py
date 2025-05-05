from locators.main_page_locators import MainPageLocators

import allure
from pages.base_page import BasePage


class MainPageYandexScooter(BasePage):

    @allure.step("Кликаем по кнопке принятия кук")
    def click_cookie_button(self):
        self.click_for_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Кликаем по верхней кнопке заказать")
    def click_top_order_button(self):
        self.click_for_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Кликаем по нижней кнопке заказать")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_for_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Кликаем по выпадающему списку")
    def click_on_drop_down_list(self, number_list):
        locator_list = MainPageLocators.number_list(number_list)
        self.scroll_to_element(locator_list)
        self.click_for_element_with_scripts(locator_list)

    @allure.step("Получаем текст выпадающего списка")
    def getting_text_drop_down_list(self, number_text):
        locator_text = MainPageLocators.number_text(number_text)
        return self.get_text_on_element(locator_text)

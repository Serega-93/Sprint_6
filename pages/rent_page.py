from selenium.webdriver import Keys

from locators.about_rent_page_locators import AboutRentPageLocators

import allure
from pages.base_page import BasePage


class AboutRentPage(BasePage):

    @allure.step("Выбираем дату доставки")
    def choosing_delivery_date(self, date):
        element = self.send_keys_to_input(AboutRentPageLocators.DELIVERY_DATE_FIELD, date)
        element.send_keys(Keys.ENTER)

    @allure.step("Выбираем срок аренды - двое суток")
    def choosing_rental_period_two_days(self):
        self.click_for_element(AboutRentPageLocators.RENTAL_PERIOD_FIELD)
        self.click_for_element(AboutRentPageLocators.TWO_DAYS_VALUE)

    @allure.step("Выбираем срок аренды - шестеро суток")
    def choosing_rental_period_six_days(self):
        self.click_for_element(AboutRentPageLocators.RENTAL_PERIOD_FIELD)
        self.click_for_element(AboutRentPageLocators.SIX_DAYS_VALUE)

    @allure.step("Выбираем цвет самоката - чёрный жемчуг")
    def choosing_black_color(self):
        self.click_for_element(AboutRentPageLocators.BLACK_COLOR)

    @allure.step("Выбираем цвет самоката - серая безысходность")
    def choosing_grey_color(self):
        self.click_for_element(AboutRentPageLocators.GREY_COLOR)

    @allure.step("Заполняем поле Комментарий курьеру")
    def fill_input_comment(self, comment):
        self.send_keys_to_input(AboutRentPageLocators.COMMENT_FIELD, comment)

    @allure.step("Кликаем по кнопке Заказать")
    def click_on_order_button(self):
        self.click_for_element(AboutRentPageLocators.BUTTON_ORDER)

    @allure.step("Кликаем по кнопке подтверждения заказа - Да")
    def click_on_button_yes(self):
        self.click_for_element(AboutRentPageLocators.BUTTON_YES)

    @allure.step("Получаем текст подтверждения заказа")
    def get_text_successful_registration(self):
        return self.get_text_on_element(AboutRentPageLocators.SUCCESSFUL_REGISTRATION_POPUP)

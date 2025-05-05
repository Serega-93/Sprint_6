from locators.registration_scooter_page_locators import RegistrationScooterPageLocators

import allure
from pages.base_page import BasePage


class RegistrationScooterPage(BasePage):

    @allure.step("Заполняем поле Имя")
    def fill_input_name(self, name):
        self.send_keys_to_input(RegistrationScooterPageLocators.NAME_FIELD, name)

    @allure.step("Заполняем поле Фамилия")
    def fill_input_last_name(self, last_name):
        self.send_keys_to_input(RegistrationScooterPageLocators.LAST_NAME_FIELD, last_name)

    @allure.step("Заполняем поле Адрес")
    def fill_input_address(self, address):
        self.send_keys_to_input(RegistrationScooterPageLocators.ADDRESS_FIELD, address)

    @allure.step("Выбираем  Станцию метро Сокольники")
    def click_input_metro_station(self):
        self.click_for_element(RegistrationScooterPageLocators.METRO_STATION_FIELD)
        self.click_for_element(RegistrationScooterPageLocators.METRO_STATION_SOCOLNIKI)

    @allure.step("Заполняем поле Телефон")
    def fill_input_phone(self, phone):
        self.send_keys_to_input(RegistrationScooterPageLocators.PHONE_FIELD, phone)

    @allure.step("Кликаем кнопку Далее")
    def click_on_button_next(self):
        self.click_for_element(RegistrationScooterPageLocators.NEXT_BUTTON)

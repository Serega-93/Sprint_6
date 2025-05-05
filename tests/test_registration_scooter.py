import allure

from pages.main_page import MainPageYandexScooter
from pages.registration_page import RegistrationScooterPage
from pages.rent_page import AboutRentPage
from helpers import generate_registration_data, tomorrow_date


class TestSuccessfulRegistrationScooter:

    @allure.title("Проверяем успешную регистрацию через верхнею кнопку Заказать")
    def test_successful_registration_for_top_order_button(self, driver):
        main_page = MainPageYandexScooter(driver)
        registration_page = RegistrationScooterPage(driver)
        rent_page = AboutRentPage(driver)
        name, last_name, address, phone, commit = generate_registration_data()
        date = tomorrow_date()
        main_page.click_cookie_button()
        main_page.click_top_order_button()
        registration_page.fill_input_name(name)
        registration_page.fill_input_last_name(last_name)
        registration_page.fill_input_address(address)
        registration_page.click_input_metro_station()
        registration_page.fill_input_phone(phone)
        registration_page.click_on_button_next()
        rent_page.choosing_delivery_date(date)
        rent_page.choosing_rental_period_two_days()
        rent_page.choosing_black_color()
        rent_page.fill_input_comment(commit)
        rent_page.click_on_order_button()
        rent_page.click_on_button_yes()
        actual_text = rent_page.get_text_successful_registration()
        expected_text = "Заказ оформлен"
        assert expected_text in actual_text

    @allure.title("Проверяем успешную регистрацию через нижнею кнопку Заказать")
    def test_successful_registration_for_bottom_order_button(self, driver):
        main_page = MainPageYandexScooter(driver)
        registration_page = RegistrationScooterPage(driver)
        rent_page = AboutRentPage(driver)
        name, last_name, address, phone, commit = generate_registration_data()
        date = tomorrow_date()
        main_page.click_cookie_button()
        main_page.click_bottom_order_button()
        registration_page.fill_input_name(name)
        registration_page.fill_input_last_name(last_name)
        registration_page.fill_input_address(address)
        registration_page.click_input_metro_station()
        registration_page.fill_input_phone(phone)
        registration_page.click_on_button_next()
        rent_page.choosing_delivery_date(date)
        rent_page.choosing_rental_period_six_days()
        rent_page.choosing_grey_color()
        rent_page.fill_input_comment(commit)
        rent_page.click_on_order_button()
        rent_page.click_on_button_yes()
        actual_text = rent_page.get_text_successful_registration()
        expected_text = "Заказ оформлен"
        assert expected_text in actual_text


from locators.registration_scooter_page_locators import RegistrationScooterPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationScooterPage:

    def __init__(self, driver):
        self.driver = driver

    def click_logo_yandex(self):
        self.driver.find_element(*RegistrationScooterPageLocators.LOGO_YANDEX).click()

    def click_logo_scooter(self):
        self.driver.find_element(*RegistrationScooterPageLocators.LOGO_SCOOTER).click()

    def set_name(self, name):
        self.driver.find_element(*RegistrationScooterPageLocators.NAME_FIELD).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*RegistrationScooterPageLocators.LAST_NAME_FIELD).send_keys(last_name)

    def set_address(self, address):
        self.driver.find_element(*RegistrationScooterPageLocators.ADDRESS_FIELD).send_keys(address)

    def set_metro_station(self, metro):
        self.driver.find_element(*RegistrationScooterPageLocators.METRO_STATION_FIELD).send_keys(metro)

    def set_phone(self, phone):
        self.driver.find_element(*RegistrationScooterPageLocators.PHONE_FIELD).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*RegistrationScooterPageLocators.NEXT_BUTTON).click()

    def wait_element_next_button(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(RegistrationScooterPageLocators.
                                                                                     NEXT_BUTTON))


from locators.about_rent_page_locators import AboutRentPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AboutRentPage:

    def __init__(self, driver):
        self.driver = driver

    def set_delivery_date(self, date):
        self.driver.find_element(*AboutRentPageLocators.DELIVERY_DATE_FIELD).send_keys(date)

    def click_rental_period(self):
        self.driver.find_element(*AboutRentPageLocators.RENTAL_PERIOD_FIELD).click()

    def choice_rental_period_two_days(self):
        self.driver.find_element(*AboutRentPageLocators.TWO_DAYS_VALUE).click()

    def choice_rental_period_six_days(self):
        self.driver.find_element(*AboutRentPageLocators.SIX_DAYS_VALUE).click()

    def click_scooter_color(self):
        self.driver.find_element(*AboutRentPageLocators.SCOOTER_COLOR_FIELD).click()

    def choice_black_color(self):
        self.driver.find_element(*AboutRentPageLocators.BLACK_COLOR).click()

    def choice_grey_color(self):
        self.driver.find_element(*AboutRentPageLocators.GREY_COLOR).click()

    def set_comment(self, comment):
        self.driver.find_element(*AboutRentPageLocators.COMMENT_FIELD).send_keys(comment)

    def click_button_order(self):
        self.driver.find_element(*AboutRentPageLocators.BUTTON_ORDER).click()

    def click_button_yes(self):
        self.driver.find_element(*AboutRentPageLocators.BUTTON_YES).click()

    def receive_text_successful_registration_popup(self):
        return self.driver.find_element(*AboutRentPageLocators.SUCCESSFUL_REGISTRATION_POPUP).text()

    def wait_element_button_yes(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(*AboutRentPageLocators.BUTTON_YES))

    def wait_element_successful_registration_popup(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(*AboutRentPageLocators.
                                                                                    SUCCESSFUL_REGISTRATION_POPUP))

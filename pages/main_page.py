from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPageYandexScooter:

    def __init__(self, driver):
        self.driver = driver

    def click_top_order_button(self):
        self.driver.find_element(*MainPageLocators.TOP_ORDER_BUTTON).click()

    def click_bottom_order_button(self):
        self.driver.find_element(*MainPageLocators.BOTTOM_ORDER_BUTTON).click()

    def click_drop_down_list_important_questions_1(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_1).click()

    def click_drop_down_list_important_questions_2(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_2).click()

    def click_drop_down_list_important_questions_3(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_3).click()

    def click_drop_down_list_important_questions_4(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_4).click()

    def click_drop_down_list_important_questions_5(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_5).click()

    def click_drop_down_list_important_questions_6(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_6).click()

    def click_drop_down_list_important_questions_7(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_7).click()

    def click_drop_down_list_important_questions_8(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_8).click()

    def wait_element_top_order_button(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(*MainPageLocators.TOP_ORDER_BUTTON))

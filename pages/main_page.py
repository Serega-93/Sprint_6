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

    def receive_text_answer_question_1(self):
        return self.driver.find_element(*MainPageLocators.TEXT_ANSWER_QUESTION_1).text

    def click_drop_down_list_important_questions_2(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_2).click()

    def receive_text_answer_question_2(self):
        return self.driver.find_element(*MainPageLocators.TEXT_ANSWER_QUESTION_2).text

    def click_drop_down_list_important_questions_3(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_3).click()

    def receive_text_answer_question_3(self):
        return self.driver.find_element(*MainPageLocators.TEXT_ANSWER_QUESTION_3).text

    def click_drop_down_list_important_questions_4(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_4).click()

    def receive_text_answer_question_4(self):
        return self.driver.find_element(*MainPageLocators.TEXT_ANSWER_QUESTION_4).text

    def click_drop_down_list_important_questions_5(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_5).click()

    def receive_text_answer_question_5(self):
        return self.driver.find_element(*MainPageLocators.TEXT_ANSWER_QUESTION_5).text

    def click_drop_down_list_important_questions_6(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_6).click()

    def receive_text_answer_question_6(self):
        return self.driver.find_element(*MainPageLocators.TEXT_ANSWER_QUESTION_6).text

    def click_drop_down_list_important_questions_7(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_7).click()

    def receive_text_answer_question_7(self):
        return self.driver.find_element(*MainPageLocators.TEXT_ANSWER_QUESTION_7).text

    def click_drop_down_list_important_questions_8(self):
        self.driver.find_element(*MainPageLocators.DROP_DOWN_LIST_IMPORTANT_QUESTIONS_8).click()

    def receive_text_answer_question_8(self):
        return self.driver.find_element(*MainPageLocators.TEXT_ANSWER_QUESTION_8).text

    def wait_element_top_order_button(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MainPageLocators.TOP_ORDER_BUTTON))

    def wait_element_drop_down_list_important_questions_8(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(MainPageLocators.
                                                                             DROP_DOWN_LIST_IMPORTANT_QUESTIONS_8))

from selenium.webdriver.common.by import By


class MainPageLocators:
    TOP_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g'] # кнопка "Заказать" вверху
    BOTTOM_ORDER_BUTTON = [By.CSS_SELECTOR, ".Home_FinishButton__1_cWm .Button_Button__ra12g"] # кнопка "Заказать" внизу
    COOKIE_BUTTON = [By.XPATH, '//button[@id="rcc-confirm-button"]']

    @staticmethod
    def number_list(lists): # выпадающий список
        return  [By.ID, f'accordion__heading-{lists}']

    @staticmethod
    def number_text(text): # текст выпадающего списка
         return [By.XPATH, f'//div[@id="accordion__panel-{text}"]/p']

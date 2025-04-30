from selenium.webdriver.common.by import By


class MainPageLocators:
    TOP_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g'] # кнопка "Заказать" вверху
    BOTTOM_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g Button_UltraBig__UU3Lp'] # кнопка "Заказать" внизу

    @staticmethod
    def number_list(list):
        return  [By.ID, f'accordion__heading-{list}']

    @staticmethod
    def number_text(text):
         return [By.XPATH, f'//div[@id="accordion__panel-{text}"]/p']

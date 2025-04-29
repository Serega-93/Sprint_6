from selenium.webdriver.common.by import By


class AboutRentPageLocators:
    DELIVERY_DATE_FIELD = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'] # поле "дата доставки самоката"
    RENTAL_PERIOD_FIELD = [By.XPATH, '//div[@class="Dropdown-placeholder"]'] # поле "срок аренды"
    DAY_VALUE = [By.XPATH, '//div[text()="сутки"]'] # сутки
    TWO_DAYS_VALUE = [By.XPATH, '//div[text()="двое суток"]'] # двое суток
    THREE_DAYS_VALUE = [By.XPATH, '//div[text()="трое суток"]'] # трое суток
    FOUR_DAYS_VALUE = [By.XPATH, '//div[text()="четверо суток"]']  # четверо суток
    FIVE_DAYS_VALUE = [By.XPATH, '//div[text()="пятеро суток"]']  # пятеро суток
    SIX_DAYS_VALUE = [By.XPATH, '//div[text()="шестеро суток"]']  # шестеро суток
    SEVEN_DAYS_VALUE = [By.XPATH, '//div[text()="семеро суток"]']  # семеро суток
    SCOOTER_COLOR_FIELD = [By.XPATH, '//div[@class="Order_Title__3EKne"]'] # поле "цвет самоката"
    BLACK_COLOR = [By.ID, 'black'] # чёрный жемчуг
    GREY_COLOR = [By.ID, 'grey'] # серая безысходность
    COMMENT_FIELD = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]'] # поле "Комментарий для курьера"
    BUTTON_ORDER = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'] # кнопка "Заказать" под формой
    BUTTON_YES = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]'] # кнопка подтверждения заказа "Да"
    SUCCESSFUL_REGISTRATION_POPUP = [By.XPATH, '//div[text()="Заказ оформлен"]'] # поп-ап "Заказ оформлен"

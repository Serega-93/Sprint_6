from selenium.webdriver.common.by import By


class AboutRentPageLocators:
    DELIVERY_DATE_FIELD = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'] # поле "дата доставки самоката"
    RENTAL_PERIOD_FIELD = [By.XPATH, '//div[@class="Dropdown-placeholder"]'] # поле "срок аренды"
    TWO_DAYS_VALUE = [By.XPATH, '//div[@class="Dropdown-option"][2]'] # двое суток
    SIX_DAYS_VALUE = [By.XPATH, '//div[@class="Dropdown-option"][6]']  # шестеро суток
    BLACK_COLOR = [By.ID, 'black'] #  цвет самоката "чёрный жемчуг"
    GREY_COLOR = [By.ID, 'grey'] # цвет самоката "серая безысходность"
    COMMENT_FIELD = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]'] # поле "Комментарий для курьера"
    BUTTON_ORDER = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'] # кнопка "Заказать" под формой
    BUTTON_YES = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]'] # кнопка подтверждения заказа "Да"
    SUCCESSFUL_REGISTRATION_POPUP = [By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]'] # поп-ап "Заказ оформлен"

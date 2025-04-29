from selenium.webdriver.common.by import By


class WhoIsTheScooterPageLocators:
    LOGO_YANDEX = [By.XPATH, '//img[@alt = "Yandex"]'] # логотип "Яндекс"
    LOGO_SCOOTER = [By.XPATH, '//img[@alt = "Scooter"]'] # логотип "Самокат"
    NAME_FIELD = [By.XPATH, '//input[@placeholder="* Имя"]'] # поле ввода "Имя"
    LAST_NAME_FIELD = [By.XPATH, '//input[@placeholder="* Фамилия"]']  # поле ввода "Фамилия"
    ADDRESS_FIELD = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'] # поле ввода "Адрес"
    METRO_STATION_FIELD = [By.XPATH, '//input[@placeholder="* Станция метро"]'] # поле ввода "Станция метро"
    PHONE_FIELD = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'] # поле ввода "Телефон"
    NEXT_BUTTON = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'] # кнопка "Далее"


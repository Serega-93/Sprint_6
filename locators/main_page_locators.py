from selenium.webdriver.common.by import By


class MainPageLocators:
    TOP_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g'] # кнопка "Заказать" вверху
    BOTTOM_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g Button_UltraBig__UU3Lp'] # кнопка "Заказать" внизу
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_1 = [By.ID, 'accordion__heading-24'] # "Сколько это стоит? И как оплатить?"
    TEXT_ANSWER_QUESTION_1 = [By.XPATH, '//div[@id="accordion__panel-24"]/p'] # ответ на первый вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_2 = [By.ID, 'accordion__heading-25'] # "Хочу сразу несколько самокатов! Так можно?"
    TEXT_ANSWER_QUESTION_2 = [By.XPATH, '//div[@id="accordion__panel-25"]/p']  # ответ на второй вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_3 = [By.ID, 'accordion__heading-26'] # "Как рассчитывается время аренды?"
    TEXT_ANSWER_QUESTION_3 = [By.XPATH, '//div[@id="accordion__panel-26"]/p']  # ответ на третий вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_4 = [By.ID, 'accordion__heading-27'] # "Можно ли заказать самокат прямо на сегодня?"
    TEXT_ANSWER_QUESTION_4 = [By.XPATH, '//div[@id="accordion__panel-27"]/p']  # ответ на четвертый вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_5 = [By.ID, 'accordion__heading-28'] # "Можно ли продлить заказ или вернуть самокат раньше?"
    TEXT_ANSWER_QUESTION_5 = [By.XPATH, '//div[@id="accordion__panel-28"]/p']  # ответ на пятый вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_6 = [By.ID, 'accordion__heading-29'] # "Вы привозите зарядку вместе с самокатом?"
    TEXT_ANSWER_QUESTION_6 = [By.XPATH, '//div[@id="accordion__panel-29"]/p']  # ответ на шестой вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_7 = [By.ID, 'accordion__heading-30'] # "Можно ли отменить заказ?"
    TEXT_ANSWER_QUESTION_7 = [By.XPATH, '//div[@id="accordion__panel-30"]/p']  # ответ на седьмой вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_8 = [By.ID, 'accordion__heading-31'] # "Я живу за МКАДом, привезёте?"
    TEXT_ANSWER_QUESTION_8 = [By.XPATH, '//div[@id="accordion__panel-31"]/p']  # ответ на восьмой вопрос

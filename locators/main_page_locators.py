from selenium.webdriver.common.by import By


class MainPageLocators:
    TOP_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g'] # кнопка "Заказать" вверху
    BOTTOM_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g Button_UltraBig__UU3Lp'] # кнопка "Заказать" внизу
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_1 = [By.ID, 'accordion__heading-0'] # "Сколько это стоит? И как оплатить?"
    TEXT_ANSWER_QUESTION_1 = [By.XPATH, '//div[@id="accordion__panel-0"]/p'] # ответ на первый вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_2 = [By.ID, 'accordion__heading-1'] # "Хочу сразу несколько самокатов! Так можно?"
    TEXT_ANSWER_QUESTION_2 = [By.XPATH, '//div[@id="accordion__panel-1"]/p']  # ответ на второй вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_3 = [By.ID, 'accordion__heading-2'] # "Как рассчитывается время аренды?"
    TEXT_ANSWER_QUESTION_3 = [By.XPATH, '//div[@id="accordion__panel-2"]/p']  # ответ на третий вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_4 = [By.ID, 'accordion__heading-3'] # "Можно ли заказать самокат прямо на сегодня?"
    TEXT_ANSWER_QUESTION_4 = [By.XPATH, '//div[@id="accordion__panel-3"]/p']  # ответ на четвертый вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_5 = [By.ID, 'accordion__heading-4'] # "Можно ли продлить заказ или вернуть самокат раньше?"
    TEXT_ANSWER_QUESTION_5 = [By.XPATH, '//div[@id="accordion__panel-4"]/p']  # ответ на пятый вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_6 = [By.ID, 'accordion__heading-5'] # "Вы привозите зарядку вместе с самокатом?"
    TEXT_ANSWER_QUESTION_6 = [By.XPATH, '//div[@id="accordion__panel-5"]/p']  # ответ на шестой вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_7 = [By.ID, 'accordion__heading-6'] # "Можно ли отменить заказ?"
    TEXT_ANSWER_QUESTION_7 = [By.XPATH, '//div[@id="accordion__panel-6"]/p']  # ответ на седьмой вопрос
    DROP_DOWN_LIST_IMPORTANT_QUESTIONS_8 = [By.ID, 'accordion__heading-7'] # "Я живу за МКАДом, привезёте?"
    TEXT_ANSWER_QUESTION_8 = [By.XPATH, '//div[@id="accordion__panel-7"]/p']  # ответ на восьмой вопрос

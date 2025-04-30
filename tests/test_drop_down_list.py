class TestDropDownListImportantQuestions:

    def test_text_answer_question_1(self, driver, main_page, element, wait):
        main_page.click_drop_down_list_important_questions_1()
        expected_result = main_page.receive_text_answer_question_1()
        actual_result = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert expected_result == actual_result

    def test_text_answer_question_2(self, driver, main_page, element, wait):
        main_page.click_drop_down_list_important_questions_2()
        expected_result = main_page.receive_text_answer_question_2()
        actual_result = ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями,'
                         ' можете просто сделать несколько заказов — один за другим.')
        assert expected_result == actual_result

    def test_text_answer_question_3(self, driver, main_page, element, wait):
        main_page.click_drop_down_list_important_questions_3()
        expected_result = main_page.receive_text_answer_question_3()
        actual_result = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                         'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                         'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
        assert expected_result == actual_result

    def test_text_answer_question_4(self, driver, main_page, element, wait):
        main_page.click_drop_down_list_important_questions_4()
        expected_result = main_page.receive_text_answer_question_4()
        actual_result = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert expected_result == actual_result

    def test_text_answer_question_5(self, driver, main_page, element, wait):
        main_page.click_drop_down_list_important_questions_5()
        expected_result = main_page.receive_text_answer_question_5()
        actual_result = ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку '
                         'по красивому номеру 1010.')
        assert expected_result == actual_result

    def test_text_answer_question_6(self, driver, main_page, element, wait):
        main_page.click_drop_down_list_important_questions_6()
        expected_result = main_page.receive_text_answer_question_6()
        actual_result = ('Самокат приезжает к вам с полной зарядкой. '
                         'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                         'Зарядка не понадобится.')
        assert expected_result == actual_result

    def test_text_answer_question_7(self, driver, main_page, element, wait):
        main_page.click_drop_down_list_important_questions_7()
        expected_result = main_page.receive_text_answer_question_7()
        actual_result = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                         'Все же свои.')
        assert expected_result == actual_result

    def test_text_answer_question_8(self, driver, main_page, element, wait):
        main_page.click_drop_down_list_important_questions_8()
        expected_result = main_page.receive_text_answer_question_8()
        actual_result = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert expected_result == actual_result

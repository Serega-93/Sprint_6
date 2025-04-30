import allure
import pytest

import data
from pages.main_page import MainPageYandexScooter


class TestDropDownListImportantQuestions:

    @allure.title("Проверяем текст выпадающего списка")
    @pytest.mark.parametrize('number_list, number_text, expected_text', data.Data.list_names)
    def test_checking_text_drop_down_list(self, driver, number_list, number_text, expected_text):
        main_page = MainPageYandexScooter(driver)
        main_page.click_on_drop_down_list(number_list)
        actual_text = main_page.getting_text_drop_down_list(number_text)
        assert actual_text == expected_text

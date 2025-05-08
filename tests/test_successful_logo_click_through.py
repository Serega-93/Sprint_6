import allure
from curl import yandex_logo_site, main_site
from pages.base_page import BasePage
from pages.main_page import MainPageYandexScooter
from pages.header_page import HeaderPage



class TestSuccessfulLogoClickThrough:

    @allure.title("Тест успешный переход по логотипу Яндекс")
    def test_successful_click_through_yandex_logo(self, driver):
        main_page = MainPageYandexScooter(driver)
        header_page = HeaderPage(driver)
        main_page.click_cookie_button()
        main_page.click_top_order_button()
        actual_url = header_page.click_on_logo_yandex()
        expected_url = yandex_logo_site
        assert actual_url == expected_url

    @allure.title("Тест успешный переход по логотипу Самокат")
    def test_successful_click_through_scooter_logo(self, driver):
        base_page = BasePage(driver)
        main_page = MainPageYandexScooter(driver)
        header_page = HeaderPage(driver)
        main_page.click_cookie_button()
        main_page.click_top_order_button()
        header_page.click_on_logo_scooter()
        actual_url = base_page.get_url_site()
        expected_url = main_site
        assert actual_url == expected_url
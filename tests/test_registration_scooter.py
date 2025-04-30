import pytest


class TestRegistrationScooter:

    @pytest.mark.parametrize('name', ['Се','Сергей','СергейСергейСер'])
    def test_registration_for_top_order_button(self, driver, registration_page, name):
        registration_page.click_top_order_button()
        registration_page.wait_element_next_button()
        registration_page.set_name(name)
        registration_page.set_last_name('Иванов')
        registration_page.set_address('Одесская 1')
        registration_page.set_metro_station('Красносельская')

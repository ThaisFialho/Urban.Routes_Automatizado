from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(5)


    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL) #URL
        urban_routes = UrbanRoutesPage(self.driver)  #Instanciando
        address_from = data.ADDRESS_FROM    #Pegando endereço De do arquivo data
        address_to = data.ADDRESS_TO    #Pegando endereço Para do arquivo data
        urban_routes.set_route(address_from, address_to)  #usando o metodo set_route do arquivo pages
        assert urban_routes.get_from_field() == address_from
        assert urban_routes.get_to_field() == address_to

    def test_select_plan(self):
        urban_routes = UrbanRoutesPage(self.driver)  #Instanciando
        urban_routes.select_supportive_plan()   #usando o metodo select_supportive_plan do arquivo pages
        assert urban_routes.get_current_selected_plan() == 'Comfort'

    def test_fill_phone_number(self):
        urban_routes = UrbanRoutesPage(self.driver)  # Instanciando
        phone_number = data.PHONE_NUMBER
        urban_routes.set_phone(phone_number)
        assert urban_routes.get_phone() == phone_number

    def test_fill_card(self):
        urban_routes = UrbanRoutesPage(self.driver)  # Instanciando
        card_number = data.CARD_NUMBER
        card_code = data.CARD_CODE
        urban_routes.set_card(card_number, card_code)
        assert urban_routes.get_current_payment_method() == 'Cartão'

    def test_comment_for_driver(self):
        urban_routes = UrbanRoutesPage(self.driver)  # Instanciando
        message = data.MESSAGE_FOR_DRIVER
        urban_routes.set_message_for_driver(message)
        assert urban_routes.get_message_for_driver() == message

    def test_order_blanket_and_handkerchiefs(self):
        urban_routes = UrbanRoutesPage(self.driver)  # Instanciando
        urban_routes.click_blanket_and_handkerchiefs_option()
        assert urban_routes.get_blanket_and_handkerchiefs_option_checked()

    def test_order_2_ice_creams(self):
        urban_routes = UrbanRoutesPage(self.driver)  # Instanciando
        urban_routes.add_ice_cream(2)
        assert urban_routes.get_amount_of_ice_cream() == 2

    def test_car_search_model_appears(self):
        urban_routes = UrbanRoutesPage(self.driver)  # Instanciando
        urban_routes.click_order_taxi_buton()
        urban_routes.wait_order_taxi_popup()
        assert urban_routes.get_order_taxi(), "O pop-up não apareceu!"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
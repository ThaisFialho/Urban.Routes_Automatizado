from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code


class UrbanRoutesPage:
#Localizadores da função test_set_route
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.XPATH, '//button[contains(text(), "Chamar um táxi")]')

#Localizadores da função test_select_plan
    supportive_plan_card = (By.XPATH, '//div[contains(@class, "tcard")]//div[contains(text(), "Comfort")]')
    active_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')

#Localizadores da função test_fill_phone_number
    phone_number_control = (By.XPATH, '//div[@class="np-button" or contains(@class, "np-button")][.//div[contains(text(), "Número de telefone")]]')
    phone_number_input = (By.ID, 'phone')
    phone_number_code_input = (By.ID, 'code')
    phone_number_next_button = (By.CSS_SELECTOR, '.full')
    phone_number_confirm_button = (By.XPATH, '//button[contains(text(), "Confirm")]')
    phone_number = (By.CLASS_NAME, 'np-text')

#Localizadores da função test_fill_card
    payment_method_select = (By.XPATH, '//div[contains(@class, "pp-button")]//div[contains(text(), "Método de pagamento")]')
    add_card_control = (By.XPATH, '//div[contains(@class, "pp-title") and contains(text(), "Adicionar cartão")]')
    card_number_input = (By.ID, 'number')
    card_plc_image = (By.CLASS_NAME, 'plc')
    card_credentials_confirm_button = (By.XPATH, '//button[contains(text(), "Adicionar")]')
    close_button_payment_method = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    current_payment_method = (By.CLASS_NAME, 'pp-value-text')

#Localizadores da função test_comment_for_driver
    message_for_driver = (By.ID, 'comment')

#Localizadores da função test_order_blanket_and_handkerchiefs
    option_switches = (By.CLASS_NAME, 'switch')
    option_switches_inputs = (By.CLASS_NAME, 'switch-input')

#Localizadores da função test_order_2_ice_creams
    add_enumerable_option = (By.CLASS_NAME, 'counter-plus')
    amount_of_enumerable_option = (By.CLASS_NAME, 'counter-value')

#Localizadores da função test_car_search_model_appears
    order_car_button = (By.CLASS_NAME, 'smart-button-wrapper')
    order_popup = (By.CLASS_NAME, 'order-body')


    def __init__(self,driver):
        self.driver = driver

# Métodos de espera
    def _wait_for(self,locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))

    def _wait_for_visible(self,locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))


# Métodos da função test_set_route
    def click_call_taxi_button(self):
        self._wait_for_visible(self.call_taxi_button).click()

    def set_route(self, from_address, to_address):
        self._wait_for_visible(self.from_field).send_keys(from_address)
        self._wait_for_visible(self.to_field).send_keys(to_address)
        self.click_call_taxi_button()
    # Para assert:
    def get_from_field(self):
        return self._wait_for(self.from_field).get_property('value')

    def get_to_field(self):
        return self._wait_for(self.to_field).get_property('value')



# Métodos da função test_select_plan
    def select_supportive_plan(self):
        card = self._wait_for_visible(self.supportive_plan_card)
        self.driver.execute_script("arguments[0].scrollIntoView();", card)
        card.click()
    # Para assert:
    def get_current_selected_plan (self):
        return self._wait_for(self.active_plan_card).text




# Métodos da função test_fill_phone_number
    def set_phone(self, number):
        self._wait_for(self.phone_number_control).click()
        self._wait_for(self.phone_number_input).send_keys(number)
        self._wait_for(self.phone_number_next_button).click()
        code = retrieve_phone_code(self.driver)
        self._wait_for(self.phone_number_code_input).send_keys(code)
        self._wait_for(self.phone_number_confirm_button).click()
    # Para assert:
    def get_phone(self):
        return self._wait_for(self.phone_number).text




# Métodos da função test_fill_card
    def set_card(self, card_number, code):
        self.driver.find_element(*self.payment_method_select).click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(*self.add_card_control).click()
        self.driver.find_element(*self.card_number_input).send_keys(card_number + Keys.TAB + code)
        self.driver.find_element(*self.card_plc_image).click()
        self.driver.find_element(*self.card_credentials_confirm_button).click()
        self.driver.find_element(*self.close_button_payment_method).click()
    # Para assert:
    def get_current_payment_method(self):
        return self._wait_for(self.current_payment_method).text



# Métodos da função test_comment_for_driver
    def set_message_for_driver(self, message):
        self._wait_for(self.message_for_driver).send_keys(message)
    # Para assert:
    def get_message_for_driver(self):
        return self._wait_for( self.message_for_driver).get_property('value')


# Métodos da função test_order_blanket_and_handkerchiefs
    def click_blanket_and_handkerchiefs_option(self):
        switches = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_all_elements_located(self.option_switches))
        switches[0].click()
    # Para assert:
    def get_blanket_and_handkerchiefs_option_checked(self):
        switches = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_all_elements_located(self.option_switches_inputs))
        return switches[0].get_property('checked')


# Métodos da função test_order_2_ice_creams
    def add_ice_cream(self, amount: int):
        option_add_controls = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_all_elements_located(self.add_enumerable_option))
        self.driver.execute_script("arguments[0].scrollIntoView();", option_add_controls[0])
        for n in range(amount):
            option_add_controls[0].click()
    # Para assert:
    def get_amount_of_ice_cream(self):
        return int(WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_all_elements_located(self.amount_of_enumerable_option))[0].text)

# Métodos da função test_car_search_model_appears
    def click_order_taxi_buton(self):
        self._wait_for(self.order_car_button).click()

    def wait_order_taxi_popup(self):
        self._wait_for_visible(self.order_popup)

    def get_order_taxi(self):
        return self._wait_for_visible(self.order_popup) is not None
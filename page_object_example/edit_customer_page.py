from page_object_example.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class EditCustomerPage(BasePage):

    @property
    def customer_id_text_field(self):
        return self.driver.find_element_by_name('cusid')

    @property
    def submit_button(self):
        return self.driver.find_element_by_name('AccSubmit')

    @property
    def reset_button(self):
        return self.driver.find_element_by_name('res')

    @property
    def address_text_field(self):
        return self.driver.find_element_by_xpath('.//textarea[@name="addr"]')

    @property
    def city_text_field(self):
        return self.driver.find_element_by_xpath('.//input[@name="city"]')

    @property
    def state_text_field(self):
        return self.driver.find_element_by_xpath('.//input[@name="state"]')

    @property
    def pin_text_field(self):
        return self.driver.find_element_by_xpath('.//input[@name="pinno"]')

    @property
    def mobile_number_text_field(self):
        return self.driver.find_element_by_xpath('.//input[@name="telephoneno"]')

    @property
    def email_text_field(self):
        return self.driver.find_element_by_xpath('.//input[@name="emailid"]')

    def open(self):
        WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located((By.XPATH, './/a[@href="EditCustomerInput.php"]')))
        self.driver.find_element_by_xpath('.//a[@href="EditCustomerInput.php"]').click()

    def edit_form(self,customer_id, click_submit=True, click_reset=False):
        self.customer_id_text_field.send_keys(customer_id)

        self.address_text_field.clear()
        self.address_text_field.send_keys('sdtfusdgsfgshdgf')
        self.city_text_field.clear()
        self.city_text_field.send_keys('aefsadf')
        self.state_text_field.clear()
        self.state_text_field.send_keys('GB')
        self.pin_text_field.clear()
        self.pin_text_field.send_keys('0987654')
        self.mobile_number_text_field.clear()
        self.mobile_number_text_field.send_keys('098765432')
        self.email_text_field.clear
        self.email_text_field.send_keys('ijodijs@wp.pl')

        if click_submit:
            self.submit_button.click()
        elif click_reset:
            self.reset_button.click()


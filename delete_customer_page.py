from page_object_example.base_page import BasePage

class DeleteCustomerPage(BasePage):

    @property
    def customer_id_text_field(self):
        return self.driver.find_element_by_name('cusid')

    @property
    def submit_button(self):
        return self.driver.find_element_by_name('AccSubmit')

    @property
    def reset_button(self):
        return self.driver.find_element_by_name('res')

    def open(self):
        self.driver.find_element_by_xpath('.//a[@href="DeleteCustomerInput.php"]').click()

    def fill_form(self,customer_id, click_submit=True, click_reset=False):
        self.customer_id_text_field.send_keys(customer_id)

        if click_submit:
            self.submit_button.click()
            alert1 = self.driver.switch_to_alert()
            alert1.accept()
            
        elif click_reset:
            self.reset_button.click()



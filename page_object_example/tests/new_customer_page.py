from page_object_example.base_page import BasePage

class NewCustomerPage(BasePage):

    @property
    def name_text_field(self):
        return self.driver.find_element_by_name('name')

    @property
    def gender_male_radio_button(self):
        return self.driver.find_element_by_xpath('.//input[@type="radio" and @value="m"]')

    @property
    def gender_female_radio_button(self):
        return self.driver.find_element_by_xpath('.//input[@type="radio" and @value="f"]')

    @property
    def birth_text_field(self):
        return self.driver.find_element_by_xpath('.//input[@name="dob"]')

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

    @property
    def password_text_field(self):
        return self.driver.find_element_by_xpath('.//input[@name="password"]')

    @property
    def submit_button(self):
        return self.driver.find_element_by_xpath('.//input[@name="sub"]')

    @property
    def reset_button(self):
        return self.driver.find_element_by_xpath('.//input[@name="res"]')

    def open(self):
        self.driver.find_element_by_xpath('.//a[@href="addcustomerpage.php"]').click()

    def fill_form(self,data,click_submit=True, click_reset=False):

        if 'customer_name' in data.keys():
            self.name_text_field.send_keys(data['customer_name'])
        if 'gender' in data.keys() and data['gender'] == 'male':
            self.gender_male_radio_button.click()
        if 'date_of_birth' in data.keys():
            self.birth_text_field.send_keys(data['date_of_birth'])
        if 'address' in data.keys():
            self.address_text_field.send_keys(data['address'])
        if 'city' in data.keys():
            self.city_text_field.send_keys(data['city'])
        if 'state' in data.keys():
            self.state_text_field.send_keys(data['state'])
        if 'pin' in data.keys():
            self.pin_text_field.send_keys(data['pin'])
        if 'mobile_number' in data.keys():
            self.mobile_number_text_field.send_keys(data['mobile_number'])
        if 'email' in data.keys():
            self.email_text_field.send_keys(data['email'])
        if 'password' in data.keys():
            self.password_text_field.send_keys(data['password'])

        if click_submit:
            self.submit_button.click()
        elif click_reset:
            self.reset_button.click()



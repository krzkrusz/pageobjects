from random import randint

from selenium.webdriver import Ie
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from page_object_example.customer_registered_successfully_page import CustomerRegisteredSuccessFullyPage
from page_object_example.delete_customer_page import DeleteCustomerPage
from page_object_example.login_page import LoginPage
from page_object_example.main_page import MainPage
from page_object_example.new_customer_page import NewCustomerPage

driver = None
# to be filled in
manager_username = 'mngr88954'
manager_password = 'UmydenE'
new_customer_id = ''
data = {'customer_name':'Jan Kowalski',
        'gender':'male',
        'date_of_birth':'12.12.1993',
        'address':'dwjijedjwe',
        'city':'Boston',
        'state':'Massachussets',
        'pin':'123456',
        'mobile_number':'123456789',
        'email': str(randint(0,100000))+'elo@ello.pl',
        'password':'okon' }


def setup_module(module):
    global driver
    caps = DesiredCapabilities.INTERNETEXPLORER
    caps['nativeEvents'] = False
    driver = Ie(capabilities=caps)
    driver.get('demo.guru99.com/V4/')


def test_login():
    login_page = LoginPage(driver)
    login_page.login_user(username=manager_username, password=manager_password)
    main_page = MainPage(driver)
    assert manager_username in main_page.manager_id_label.text

def test_new_customer():
    new_customer_page = NewCustomerPage(driver)
    new_customer_page.open()
    new_customer_page.fill_form(data)

    customer_registered_page = CustomerRegisteredSuccessFullyPage(driver)
    assert customer_registered_page.get_title() == 'Customer Registered Successfully!!!'
    global new_customer_id
    new_customer_id = customer_registered_page.get_customer_id()

def test_delete_customer_succesfully(customer_id=new_customer_id):
    delete_page = DeleteCustomerPage(driver)
    delete_page.open()
    alert_text = delete_page.fill_form(customer_id=new_customer_id)
    assert alert_text == 'Customer deleted Successfully'

def test_delete_customer_not_successfully(customer_id=new_customer_id):
    delete_page = DeleteCustomerPage(driver)
    delete_page.open()
    alert_text = delete_page.fill_form(customer_id=new_customer_id)
    assert alert_text == 'Customer does not exist!!'

def teardown_module(module):
    global driver
    # driver.quit()
    driver = None

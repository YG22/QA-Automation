import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.color import Color


# precondition
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()


list_of_users = [["Alfreds", "Stutterer"], ["Blondel", "Pereett"], ["Centrot", "Moctezuman"],
                 ["Easternaan", "Connecti "], ["Ernston", "Handelle"]]


# *** Test Cases ***

def test_sanity(setup):
    driver = setup
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys("yafithadar1@gmail.com")
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("yafit123#")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    select_sides(setup)
    click_reserve_button(setup)
    total = get_total_value_from_summary_page(setup)
    table_no = get_table_no_from_summary_page(setup)
    click_on_send_button(setup)
    total_from_success_page = get_total_value_from_ordering_success_page(setup)
    table_no_from_success_page = get_table_no_from_ordering_success_page(setup)
    assert total_from_success_page == total and table_no_from_success_page == table_no


def test_sign_in(setup):
    driver = setup
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys("gerafos8@walla.com")
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("221093yossi")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    select_combo_meal(setup)
    click_reserve_button(setup)
    total = get_total_value_from_summary_page(setup)
    table_no = get_table_no_from_summary_page(setup)
    click_on_send_button(setup)
    total_from_success_page = get_total_value_from_ordering_success_page(setup)
    table_no_from_success_page = get_table_no_from_ordering_success_page(setup)
    assert total_from_success_page == total and table_no_from_success_page == table_no


def test_sign_up(setup):
    driver = setup
    first_sign_up_btn = driver.find_element(By.XPATH, '//a[@href="#/SignUp"]')
    first_sign_up_btn.click()
    email_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    email_of_sign_up.send_keys(list_of_users[0][0] + "@gmail.com")
    password_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]')
    password_of_sign_up.send_keys(list_of_users[0][0] + "123$")
    confirm_password = driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]')
    confirm_password.send_keys(list_of_users[0][0] + "123$")
    second_sign_up_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    second_sign_up_btn.click()
    select_burger(setup)
    click_reserve_button(setup)
    total = get_total_value_from_summary_page(setup)
    table_no = get_table_no_from_summary_page(setup)
    click_on_send_button(setup)
    total_from_success_page = get_total_value_from_ordering_success_page(setup)
    table_no_from_success_page = get_table_no_from_ordering_success_page(setup)
    assert total_from_success_page == total and table_no_from_success_page == table_no


def test_reservation_order(setup):
    driver = setup
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys("gerafos8@walla.com")
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("221093yossi")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    select_combo_meal(setup)
    select_burger(setup)
    click_reserve_button(setup)
    total = get_total_value_from_summary_page(setup)
    table_no = get_table_no_from_summary_page(setup)
    click_on_send_button(setup)
    total_from_success_page = get_total_value_from_ordering_success_page(setup)
    table_no_from_success_page = get_table_no_from_ordering_success_page(setup)
    assert total_from_success_page == total and table_no_from_success_page == table_no


# *** Suite 1 --> Sign In
# ===> Functionality

my_email_and_password = [["gerafos8@walla.com", "221093yossi"], ["yafithadar1@gmail.com", "yafit123#"],
                         ["yafit.s@yahoo.co.il", "testing123##"]]


@pytest.mark.parametrize("my_user", my_email_and_password)
def test_log_in_via_walla_gmail_yahoo(setup, my_user):
    driver = setup
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys(my_user[0])
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys(my_user[1])
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    log_in_success = driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]')
    assert log_in_success.is_displayed()


# ===> Error Handling

def test_log_in_without_insert_an_email(setup):
    driver = setup
    alert = Alert(driver)
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("testing123##")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    time.sleep(0.5)
    alert_message = alert.text
    alert.accept()
    assert alert_message == "Failed to log in"


def test_log_in_with_wrong_password(setup):
    driver = setup
    alert = Alert(driver)
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys("yafit.s@yahoo.co.il")
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("yafit123!!")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    time.sleep(0.5)
    alert_message = alert.text
    alert.accept()
    assert alert_message == "Failed to log in"


# *** Suite 2 --> Sign Up
# ===> Functionality

def test_sign_up_only_with_required_fields(setup):
    driver = setup
    first_sign_up_btn = driver.find_element(By.XPATH, '//a[@href="#/SignUp"]')
    first_sign_up_btn.click()
    email_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    email_of_sign_up.send_keys(list_of_users[1][0] + "@walla.com")
    password_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]')
    password_of_sign_up.send_keys(list_of_users[1][0] + "175!")
    confirm_password = driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]')
    confirm_password.send_keys(list_of_users[1][0] + "175!")
    second_sign_up_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    second_sign_up_btn.click()
    log_in_success = driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]')
    assert log_in_success.is_displayed()


def test_sign_up_with_a_first_name_that_contains_7_chars(setup):
    driver = setup
    first_sign_up_btn = driver.find_element(By.XPATH, '//a[@href="#/SignUp"]')
    first_sign_up_btn.click()
    first_name = driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]')
    first_name.send_keys(list_of_users[2][0])
    email_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    email_of_sign_up.send_keys(list_of_users[2][0] + "@gmail.com")
    password_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]')
    password_of_sign_up.send_keys(list_of_users[2][0] + "14%")
    confirm_password = driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]')
    confirm_password.send_keys(list_of_users[2][0] + "14%")
    second_sign_up_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    second_sign_up_btn.click()
    confirmation_registration = driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]')
    assert confirmation_registration.is_displayed()


def test_sign_up_with_10_chars_on_first_name(setup):
    driver = setup
    first_sign_up_btn = driver.find_element(By.XPATH, '//a[@href="#/SignUp"]')
    first_sign_up_btn.click()
    first_name = driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]')
    first_name.send_keys(list_of_users[3][0])
    email_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    email_of_sign_up.send_keys(list_of_users[3][0] + "@gmail.com")
    password_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]')
    password_of_sign_up.send_keys(list_of_users[3][0] + "554")
    confirm_password = driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]')
    confirm_password.send_keys(list_of_users[3][0] + "554")
    second_sign_up_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    second_sign_up_btn.click()
    confirmation_registration = driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]')
    assert confirmation_registration.is_displayed()


def test_sign_up_with_10_chars_on_last_name(setup):
    driver = setup
    first_sign_up_btn = driver.find_element(By.XPATH, '//a[@href="#/SignUp"]')
    first_sign_up_btn.click()
    last_name = driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]')
    last_name.send_keys(list_of_users[2][1])
    email_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    email_of_sign_up.send_keys(list_of_users[2][0] + "@gmail.com")
    password_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]')
    password_of_sign_up.send_keys(list_of_users[2][0] + "14%")
    confirm_password = driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]')
    confirm_password.send_keys(list_of_users[2][0] + "14%")
    second_sign_up_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    second_sign_up_btn.click()
    confirmation_registration = driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]')
    assert confirmation_registration.is_displayed()


# ===> Error Handling


def test_sign_up_without_inserting_an_email(setup):
    driver = setup
    first_sign_up_btn = driver.find_element(By.XPATH, '//a[@href="#/SignUp"]')
    first_sign_up_btn.click()
    password_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]')
    password_of_sign_up.send_keys(list_of_users[2][0] + "14%")
    confirm_password = driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]')
    confirm_password.send_keys(list_of_users[2][0] + "14%")
    second_sign_up_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    second_sign_up_btn.click()
    prompt_validation = driver.switch_to.active_element
    message_validation = prompt_validation.get_attribute("validationMessage")
    assert message_validation == "Fill this field"


def test_sign_up_without_inserting_a_password(setup):
    driver = setup
    first_sign_up_btn = driver.find_element(By.XPATH, '//a[@href="#/SignUp"]')
    first_sign_up_btn.click()
    email_of_sign_up = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    email_of_sign_up.send_keys(list_of_users[4][0] + "@gmail.com")
    confirm_password = driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]')
    confirm_password.send_keys(list_of_users[4][0] + "32^")
    second_sign_up_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    second_sign_up_btn.click()
    prompt_validation = driver.switch_to.active_element
    message_validation = prompt_validation.get_attribute("validationMessage")
    assert message_validation == "Fill this field"


# *** Suite 3 --> Reservation and confirm reservation
# ===> Functionality


def test_order_2_meals(setup):
    driver = setup
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys("gerafos8@walla.com")
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("221093yossi")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    select_combo_meal(setup)
    select_vegan(setup)
    click_reserve_button(setup)
    total = get_total_value_from_summary_page(setup)
    table_no = get_table_no_from_summary_page(setup)
    click_on_send_button(setup)
    total_from_success_page = get_total_value_from_ordering_success_page(setup)
    table_no_from_success_page = get_table_no_from_ordering_success_page(setup)
    assert total_from_success_page == total and table_no_from_success_page == table_no


def test_select_same_meal_twice_to_cancel_order(setup):
    driver = setup
    action = ActionChains(driver)
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys("yafithadar1@gmail.com")
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("yafit123#")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    select_combo_meal(setup)
    select_combo_meal(setup)
    reserve_btn = driver.find_element(By.XPATH, '//button[text()=" Reserve "]')
    action.move_to_element(reserve_btn).perform()
    assert not reserve_btn.is_enabled()


def test_order_two_meals_to_table_no_2(setup):
    driver = setup
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys("yafithadar1@gmail.com")
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("yafit123#")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    select_combo_meal(setup)
    select_vegan(setup)
    click_reserve_button(setup)
    total = get_total_value_from_summary_page(setup)
    set_table_number_field(setup)
    table_no = get_table_no_from_summary_page(setup)
    click_on_send_button(setup)
    total_from_success_page = get_total_value_from_ordering_success_page(setup)
    table_no_from_success_page = get_table_no_from_ordering_success_page(setup)
    assert total_from_success_page == total and table_no_from_success_page == table_no


def test_press_on_log_out_button(setup):
    driver = setup
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys("yafithadar1@gmail.com")
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("yafit123#")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    click_log_out(setup)
    home_page = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/p[1]')
    assert home_page.is_displayed()


def test_order_3_meals(setup):
    driver = setup
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys("yafithadar1@gmail.com")
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("yafit123#")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    select_burger(setup)
    select_combo_meal(setup)
    select_vegan(setup)
    click_reserve_button(setup)
    total = get_total_value_from_summary_page(setup)
    table_no = get_table_no_from_summary_page(setup)
    click_on_send_button(setup)
    total_from_success_page = get_total_value_from_ordering_success_page(setup)
    table_no_from_success_page = get_table_no_from_ordering_success_page(setup)
    assert total_from_success_page == total and table_no_from_success_page == table_no


# ===> Error Handling

def test_insert_3_on_quantity(setup):
    driver = setup
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys("yafithadar1@gmail.com")
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("yafit123#")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    select_kids_meal(setup)
    click_reserve_button(setup)
    set_quantity_field(setup)
    prompt_validation = driver.switch_to.active_element
    message_validation = prompt_validation.get_attribute("validationMessage")
    click_on_send_button(setup)
    assert message_validation == "Invalid value in quantity"


def test_select_4_meals(setup):
    driver = setup
    name_color = ""
    first_sign_in_btn = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    first_sign_in_btn.click()
    e_mail = driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]')
    e_mail.send_keys("yafithadar1@gmail.com")
    password = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
    password.send_keys("yafit123#")
    second_sign_in_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    second_sign_in_btn.click()
    select_burger(setup)
    select_kids_meal(setup)
    select_vegan(setup)
    select_sides(setup)
    sides_div = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[5]/div')
    color_after_clicked = sides_div.value_of_css_property("background-color")
    color_after_clicked = Color.from_string(color_after_clicked).hex
    if color_after_clicked == "#add8e6":
        name_color += "blue"
    else:
        name_color += "white"
    assert name_color == "white"


# A function that performs a click on the "combo" meal
def select_combo_meal(setup):
    driver = setup
    combo_meal = driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]')
    combo_meal.click()


# A function that performs a click on the "kids" meal
def select_kids_meal(setup):
    driver = setup
    kids_meal = driver.find_element(By.XPATH, '//h5[text()="Kids Meal"]')
    kids_meal.click()


# A function that performs a click on the "burger" meal
def select_burger(setup):
    driver = setup
    burger = driver.find_element(By.XPATH, '//h5[text()="Burger"]')
    burger.click()


# A function that performs a click on the "vegan" meal
def select_vegan(setup):
    driver = setup
    action = ActionChains(driver)
    vegan = driver.find_element(By.XPATH, '//h5[text()="Vegan"]')
    action.move_to_element(vegan).perform()
    vegan.click()


# A function that performs a click on the "sides" meal
def select_sides(setup):
    driver = setup
    action = ActionChains(driver)
    sides = driver.find_element(By.XPATH, '//h5[text()="Sides"]')
    time.sleep(2)
    action.move_to_element(sides).perform()
    sides.click()


# A function that performs a click on the "reserve" button
def click_reserve_button(setup):
    driver = setup
    action = ActionChains(driver)
    reserve_btn = driver.find_element(By.XPATH, '//button[text()=" Reserve "]')
    time.sleep(2)
    action.move_to_element(reserve_btn).perform()
    reserve_btn.click()


# A function that performs a click on the "logout" button
def click_log_out(setup):
    driver = setup
    action = ActionChains(driver)
    log_out_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[1]')
    time.sleep(2)
    action.move_to_element(log_out_btn).perform()
    log_out_btn.click()


# A function that clears the "quantity" field and sends the number 3
def set_quantity_field(setup):
    driver = setup
    quantity = driver.find_element(By.XPATH, '//input[@Index=0]')
    quantity.clear()
    quantity.send_keys("3")


# A function that clears the "table no" field and sends the number 2
def set_table_number_field(setup):
    driver = setup
    table_no = driver.find_element(By.XPATH, '//input[@max=99]')
    table_no.clear()
    table_no.send_keys("2")


# A function that performs a click on the "send" button
def click_on_send_button(setup):
    driver = setup
    action = ActionChains(driver)
    send_btn = driver.find_element(By.XPATH, '//button[text()="Send"]')
    action.move_to_element(send_btn).perform()
    send_btn.click()


# A function that takes the text from summary page and converts it to a "float" number
# and returns the "total" value as a "float" variable
def get_total_value_from_summary_page(setup):
    driver = setup
    total = driver.find_element(By.XPATH, '//div[contains(text(),"Total: ")]').text
    total = float(total[7:-1])
    return total


# A function that takes the value from summary page and returns
# the variable "table no" and returns it as a string variable
def get_table_no_from_summary_page(setup):
    driver = setup
    table_no = driver.find_element(By.XPATH, '//input[@max=99]').get_attribute('value')
    return table_no


# A function that takes the text from ordering success page and converts it to a "float" number
# and returns the "total" value as a "float" variable
def get_total_value_from_ordering_success_page(setup):
    driver = setup
    total = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/h2[1]').text
    total = float(total[7:-1])
    return total


# A function that takes the value from ordering success page and returns
# the variable "table no" and returns it as a string variable
def get_table_no_from_ordering_success_page(setup):
    driver = setup
    table_no = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/'
                                             'div/div/div[2]/h3[2]').text
    return table_no[-1]

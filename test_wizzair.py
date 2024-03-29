# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import test_data
import time

class WizzairRegistartionTest(unittest.TestCase):
    """
    Class for registration on wizzair.com/pl-pl/
    """
    def setUp(self):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://wizzair.com/pl-pl/main-page#/")


    def tearDown(self):
        self.driver.quit()

    def test_wrong_email(self):
        driver = self.driver
        zaloguj_btn = driver.find_element_by_class_name("rf-mobile-login__logged-out")
        zaloguj_btn.click()
        rejestracja_btn = driver.find_element_by_xpath("//button[text()='Rejestracja']")
        rejestracja_btn.click()
        name_field = driver.find_element_by_xpath('//input[@placeholder="Imię"]')
        name_field.send_keys(test_data.valid_name)
        surname_field = driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        surname_field.send_keys(test_data.valid_surname)
        if test_data.sex == 'male':
            gender_switch = driver.find_element_by_xpath("//label[@for='register-gender-male']")
            driver.execute_script("arguments[0].click()", gender_switch)
        else:
            gender_switch = driver.find_element_by_xpath("//label[@for='register-gender-female']")
            driver.execute_script("arguments[0].click()", gender_switch)
        telephone_field = driver.find_element_by_name("mobilePhone")
        telephone_field.send_keys(test_data.valid_telephone)
        email_field =  driver.find_element_by_css_selector("input[placeholder='E-mail'][data-test='booking-register-email']")
        email_field.send_keys(test_data.invalid_email)
        password_field = driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
        password_field.send_keys(test_data.valid_password)
        country_field = driver.find_element_by_xpath("//input[@data-test='booking-register-country']")
        country_field.click()
        country_to_choose = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        countries = country_to_choose.find_elements_by_xpath("label")
        print(test_data.country)
        for label in countries:
            d=label.find_element_by_tag_name('strong')
            # print(d.text)
            if d.get_attribute("innerText") == test_data.country:
                d.location_once_scrolled_into_view
                d.click()
                break



if __name__== '__main__':
    unittest.main(verbosity=2)

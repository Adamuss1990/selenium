# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

gender = 'male'

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def tearDown(self):
        self.driver.quit()

    def test_wrong_email(self):
        driver = self.driver

        #ze względu na znikanie zaloguj
        rejestracja = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[data-test=navigation-menu-signin]")))
        rejestracja.click()

        rejestr = driver.find_element_by_xpath(
        '//button[text()="Rejestracja"]')
        rejestr.click()

        imie_field = driver.find_element_by_name("firstName")
        imie = 'Adam'
        imie_field.send_keys(imie)

        nazwisko_field = driver.find_element_by_xpath('//input[@data-test="registrationmodal-last-name-input"]')
        nazwisko = 'xxxx'
        nazwisko_field.send_keys(nazwisko)

        if gender == 'male':
            m = driver.find_element_by_xpath('//label[@for="register-gender-male"]')
            imie_field.click()
            m.click()
        else:
            f = driver.find_element_by_xpath('//label[@for="register-gender-female"]')
            f.click()


        telefon = driver.find_element_by_xpath('//input[@placeholder="Telefon komórkowy"]')
        kom_zam = '48 32 1234567'
        telefon.send_keys(kom_zam)


        #błędny email
        email = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        email_zam = 'adamuss7vp.pl'
        email.send_keys(email_zam)


        haslo = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        haslo_zam = 'Adamuss7'
        haslo.send_keys(haslo_zam)


        narodowosc = driver.find_element_by_xpath(
        '//input[@data-test="booking-register-country"]')
        narodowosc.click()
        szukanie_kraju = driver.find_element_by_xpath(
        '//label[@data-test="booking-register-country-label"][164]')
        szukanie_kraju.location_once_scrolled_into_view
        szukanie_kraju.click()

        zatwierdz = driver.find_element_by_xpath(
        ' //label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        zatwierdz.click()

        register_btn = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        register_btn.click()

        #Test - znajdz wszystkie błedy

        error_notices = self.driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        visible_error_notices = []

        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)

        len(visible_error_notices) == 1
        error_text = visible_error_notices[0].get_attribute("innerText")
        print "\n" + error_text
        self.assertEqual(error_text, u"Nieprawidłowy adres e-mail")

        sleep(2)



if __name__ == '__main__':
    unittest.main(verbosity=3)

#Rejestracja nowego użytkownika na stronie wizzair.com

#Przypadki testowe:
#I Rejestracja nowego użytkownika używając adresu email - dane niepoprawne (niekompletny email)

#Warunki wstępne:
#Przeglądarka otwarta na https://wizzair.com/pl-pl/main-page#/

#Kroki:
#1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
#2. Wybierz rejestracja
#3. Wprowadź imię
#4. Wprowadź nazwisko
#5. Wybierz płeć
#6. Wprowadź nr tel
#7. Wprowadź błędny adres email - brak znaku @
#8. Wprowadź hasło
#9. Wybierz kraj
#10. Akceptuj politykę prywatności
#11. Kliknij przycisk ZAREJESTRUJ SIĘ"

#Oczekiwany rezultat:
#1. Przycisk "zarejestruj się" jest nieaktywny
#2. Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny

# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import time

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def tearDown(self):
        self.driver.quit()

    def test_wrong_email(self):
        driver = self.driver

        rejestracja = driver.find_element_by_xpath(
        '//button[@data-test="navigation-menu-signin"]')
        rejestracja.click()
        time.sleep(3)




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

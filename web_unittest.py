# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest

#klasa dziedzicząca po klasie
#TestCase z modułu unittest
class WsbPLCheck(unittest.TestCase):
    #instrukcje, jako warunki początkowe
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    #instrukcje, wykonywane po każdym tescie
    def tearDown(self):
        self.driver.quit()

    #Testy zaczynają się do sowa testself.
    def test_numer_jeden(self):
        #kroki testowe
        driver = self.driver
        driver.get("http://www.wsb.pl")

        self.assertIn(u"Wyższe Szkoły Bankowe", driver.title)
        assert u"Wyższe Szkoły Bankowe" in driver.title



    def test_kolejny(self):
        pass
    def test_ostatni_test(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=3)

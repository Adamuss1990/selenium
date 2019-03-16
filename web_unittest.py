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

        webelement = self.driver.find_element_by_tag_name("body")
        driver.find_element_by_id("edit-city")
        lupa = driver.find_element_by_class_name("search-icon")
        link = driver.find_element_by_link_text("Kontakt")
        kontakt = driver.find_element_by_partial_link_text("Kont")
        kontakt.click()
        driver.find_element_by_name("city")

    def test_ostatni_test(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=3)

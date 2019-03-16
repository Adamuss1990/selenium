# -*- coding: utf-8 -*-

from selenium import webdriver
import time

#nowy sterownik dla firefox
driver = webdriver.Chrome()
#zwiększ okno
driver.maximize_window()
#zmiana strony
driver.get("http://www.wsb.pl")
time.sleep(3)
#zamknięcie przeglądarki
driver.quit()

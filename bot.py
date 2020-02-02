from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class Bot():
    url = 'https://fb.com/'
    search_person = 'Mesti Nesibov'
    # sifre = os.environ.get('sifre')
    # parol = os.environ.get('parol')
    # code = os.environ.get('code')
    def __init__(self):
        self.goto_site()

    def goto_site(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("dom.webnotifications.enabled", False)
        self.browser_driver = webdriver.Firefox(firefox_profile=profile, executable_path='/home/idris/Desktop/geckodriver')
        self.browser_driver.get(self.url)
        self.login()

    def login(self):
        self.browser_driver.find_element_by_name('email').send_keys('idris1996@bk.ru')
        self.browser_driver.find_element_by_name('pass').send_keys(os.environ.get('sifre'))
        self.browser_driver.find_element_by_css_selector("#loginbutton>[type='submit']").click()
        self.search_mesti()

    def search_mesti(self):
        self.browser_driver.get(f'https://www.facebook.com/search/top/?q={self.search_person}')
        self.browser_driver.find_element_by_css_selector('._6xu4._6xu5.img').click()
        self.goto_profile_image()

    def goto_profile_image(self):
        time.sleep(10)
        self.browser_driver.find_element_by_css_selector('._11kf.img').click()
        time.sleep(20)
        self.browser_driver.find_element_by_css_selector('._6a-y').click()

        # elements=self.browser_driver.find_elements_by_css_selector('')
        # elements[0].click()

Bot()

from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

email= 'ewamroczek@ewaa.com'
haslo= 'ewamroczek'


class APRegistration(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions();
        options.set_preference("browser.link.open_newwindow", 1);
        self.driver = webdriver.Firefox(options=options)
        #self.driver.maximize_window()
        self.driver.get('http://dinette.pl')


    def testCorrectRegistration(self):
        driver = self.driver
        #Odnajdz Sklep Online
        sklep_online = driver.find_element_by_partial_link_text('Sklep Online')
        #1.Kliknij
        sklep_online.click()
        #kliknij "Pieczywo"
        xpath = '//a[contains(@href,"/collections/pieczywo")]'
        def get_and_refresh(dr):
            return dr.find_element(By.XPATH, xpath)
        #pieczywo =
        pieczywo =  WebDriverWait(driver, 10).until(lambda driver : get_and_refresh(driver))
        print(pieczywo)
        pieczywo.click()

        #kliknij "Bajgle"
        xpath = '//a[contains(@href,"/collections/pieczywo/products/bajgle")]'
        def get_and_refresh(dr):
            return dr.find_element(By.XPATH, xpath)
        #bajgle
        bajgle = WebDriverWait(driver, 10).until(lambda driver : get_and_refresh(driver))
        print(bajgle)
        bajgle.click()
        sleep(3)
        #kup teraz
        driver.find_element_by_css_selector('.shopify-payment-button__button').click()
        sleep(3)
        #wpisz email
        email_input =  driver.find_element_by_id('CustomerEmail')
        email_input.send_keys(email)
        #wpisz haslo
        password_input = driver.find_element_by_id('CustomerPassword')
        password_input.send_keys(haslo)
        sleep(3)

    def tearDown(self):
            self.driver.quit()



if __name__=='__main__':
    unittest.main(verbosity=2)

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from settings import ConfigSettings

class UserLogin(unittest.TestCase):
    cfg = ConfigSettings("config.ini")

    @classmethod
    def setUpClass(self):
        driverPath=self.cfg.getConfigSetting('BrowserType','driver')
        self.driver = webdriver.Chrome(driverPath)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self.cfg.getConfigSetting('EndPoint','AdminURL'))

    def test_login(self):
        userName=self.cfg.getConfigSetting('Credentials','login')
        password=self.cfg.getConfigSetting('Credentials','password')
        self.search_field = self.driver.find_element_by_name("username")
        self.search_field.send_keys(userName)
        self.search_field = self.driver.find_element_by_name("password")
        self.search_field.send_keys(password)
        self.search_field.submit()
        element = self.driver.find_element_by_xpath('//a[contains(@href, "%s")]' % "logout")
        self.assertEqual("logout", element.text.encode('ascii', 'ignore').lower())
        element.click()

    def test_logout(self):
        userName=self.cfg.getConfigSetting('Credentials','login')
        password=self.cfg.getConfigSetting('Credentials','password')
        self.search_field = self.driver.find_element_by_name("username")
        self.search_field.send_keys(userName)
        self.search_field = self.driver.find_element_by_name("password")
        self.search_field.send_keys(password)
        self.search_field.submit()
        element = self.driver.find_element_by_xpath('//a[contains(@href, "%s")]' % "logout")
        element.click()
        button = self.driver.find_elements_by_xpath("//input[@value='Sign in']")
        self.assertTrue(button)
    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':

    unittest.main()

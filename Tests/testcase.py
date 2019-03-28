import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/usr/local/bin/WebDriver/chromedriver")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://admin-uat.firstfuelsoftware.net/ff_auth/login")
    def test_login(self):
        self.search_field = self.driver.find_element_by_name("username")
        self.search_field.send_keys("amitd")
        self.search_field = self.driver.find_element_by_name("password")
        self.search_field.send_keys("Test1234$")
        self.search_field.submit()
        text="logout"
        element = self.driver.find_element_by_xpath('//a[contains(@href, "%s")]' % text)
        self.assertEqual("logout", element.text.encode('ascii', 'ignore').lower())

    def test_logout(self):
        self.search_field = self.driver.find_element_by_name("username")
        self.search_field.send_keys("amitd")
        self.search_field = self.driver.find_element_by_name("password")
        self.search_field.send_keys("Test1234$")
        self.search_field.submit()
        element = self.driver.find_element_by_xpath('//a[contains(@href, "%s")]' % "logout")
        element.click()
        button = self.driver.find_elements_by_xpath("//input[@value='Sign in']")

        self.assertTrue(button)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

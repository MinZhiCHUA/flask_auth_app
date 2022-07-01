import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

class Index_main(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://mz-monitoring-flask-v2.azurewebsites.net/")
        self.assertIn("Flask", driver.title)
        elem = driver.find_element(By.NAME, "flasktitle")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.close()

class Index_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_search_in_login(self):
        driver = self.driver
        driver.get("http://mz-monitoring-flask-v2.azurewebsites.net/")

        elem = driver.find_element(By.LINK_TEXT, "Login")
        elem.click()
        # self.assertIn("Login", driver.title)
        self.assertIn("http://mz-monitoring-flask-v2.azurewebsites.net/login", driver.current_url)

    def tearDown(self):
        self.driver.close()

class Index_Signup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_search_in_signup(self):
        driver = self.driver
        driver.get("http://mz-monitoring-flask-v2.azurewebsites.net/")

        elem = driver.find_element(By.LINK_TEXT, "Sign Up")
        elem.click()
        # self.assertIn("Login", driver.title)
        self.assertIn("http://mz-monitoring-flask-v2.azurewebsites.net/signup", driver.current_url)

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
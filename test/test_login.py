import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

import time 

class Login_main_auth_user(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_login_main(self):
        driver = self.driver
        driver.get("http://mz-monitoring-flask-v2.azurewebsites.net/login")
        # self.assertIn("Login", driver.title)
        driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("abcabc@gmail.com")
        # elem.send_keys(Keys.RETURN)
        # time.sleep(10)
        
        elem2 = driver.find_element(By.NAME, "password")
        elem2.send_keys("abcabc")
        # elem2.send_keys(Keys.RETURN)
        # time.sleep(5)

        elem3 = driver.find_element(By.ID, "btn_login")
        elem3.click()

        time.sleep(1)

        self.assertIn("http://mz-monitoring-flask-v2.azurewebsites.net/profile", driver.current_url)
        # print(driver.page_source)

        test_elem = driver.find_element(By.CLASS_NAME, "profile_title")
        print (test_elem.text)

        self.assertEqual("Welcome, ABC ABC!\nHey hey hey you are just a regular user", test_elem.text)
        # self.assertIn("Welcome ABC ABC" not in driver.page_source)

        # self.assertNotIn("No results found.", driver.page_source)
        driver.find_element(By.LINK_TEXT, "Logout").click()
        self.assertIn("http://mz-monitoring-flask-v2.azurewebsites.net/", driver.current_url)

    def tearDown(self):
        self.driver.close()

class Login_main_auth_admin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_Login_main_auth_admin(self):
        driver = self.driver
        driver.get("http://mz-monitoring-flask-v2.azurewebsites.net/login")
        # self.assertIn("Login", driver.title)
        driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("admin@gmail.com")
        # elem.send_keys(Keys.RETURN)
        # time.sleep(10)
        
        elem2 = driver.find_element(By.NAME, "password")
        elem2.send_keys("admin")
        # elem2.send_keys(Keys.RETURN)
        # time.sleep(5)

        elem3 = driver.find_element(By.ID, "btn_login")
        elem3.click()

        time.sleep(1)

        self.assertIn("http://mz-monitoring-flask-v2.azurewebsites.net/profile", driver.current_url)
        # print(driver.page_source)

        test_elem = driver.find_element(By.CLASS_NAME, "profile_title")
        print (test_elem.text)

        self.assertEqual("Welcome, Admin: Min Zhi!\nThis is super secret content only for admin", test_elem.text)
        # self.assertIn("Welcome ABC ABC" not in driver.page_source)

        # self.assertNotIn("No results found.", driver.page_source)
        driver.find_element(By.LINK_TEXT, "Logout").click()
        self.assertIn("http://mz-monitoring-flask-v2.azurewebsites.net/", driver.current_url)

    def tearDown(self):
        self.driver.close()

class Login_main_unauthorize(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_login_main(self):
        driver = self.driver
        driver.get("http://mz-monitoring-flask-v2.azurewebsites.net/login")
        
        driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("dgfdfdgfd@gmail.com")
        
        elem2 = driver.find_element(By.NAME, "password")
        elem2.send_keys("fgdgdfg")
  
        elem3 = driver.find_element(By.ID, "btn_login")
        elem3.click()

        time.sleep(1)

        self.assertNotIn("http://mz-monitoring-flask-v2.azurewebsites.net/profile", driver.current_url)
        # self.assertIn(True, driver.find_element(By.CLASS_NAME, "notification is-danger").is_displayed())
        # self.assertIn(True, driver.find_element(By.CSS_SELECTOR, "notification").is_displayed())


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
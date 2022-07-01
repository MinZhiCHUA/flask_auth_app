import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time 

class Login_main_auth(unittest.TestCase):

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

        time.sleep(3)

        self.assertIn("http://mz-monitoring-flask-v2.azurewebsites.net/profile", driver.current_url)
        # print(driver.page_source)

        test_elem = driver.find_element(By.CLASS_NAME, "profile_title")
        print (test_elem.text())

        # self.assertEquals("Welcome ABC ABC", test_elem.getText())
        # self.assertIn("Welcome ABC ABC" not in driver.page_source)

        # self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
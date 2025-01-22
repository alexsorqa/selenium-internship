from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SignInPage(BasePage):
    EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-button")

    def login_sign_in_page(self, email, password):
        self.driver.wait.until(EC.url_to_be('https://soft.reelly.io/sign-in'))
        #sleep(2)
        self.wait_for_element_visible(*self.EMAIL)
        #sleep(2)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        #sleep(2)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        #sleep(2)
        self.wait_and_click(*self.LOGIN_BUTTON)




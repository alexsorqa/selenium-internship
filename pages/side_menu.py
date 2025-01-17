from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SideMenu(BasePage):
    OFF_PLAN = (By.CSS_SELECTOR, ".menu_block_1 .menu-twobutton")
    OFF_PLAN_TEXT = (By.CSS_SELECTOR, ".off_plan")

    def click_on_off_plan(self):
        self.click(*self.OFF_PLAN)
        self.wait_for_element_visible(self.OFF_PLAN_TEXT)


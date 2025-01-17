from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.side_menu import SideMenu
from pages.off_plan_page import OffPlanPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.side_menu = SideMenu(driver)
        self.off_plan_page = OffPlanPage(driver)
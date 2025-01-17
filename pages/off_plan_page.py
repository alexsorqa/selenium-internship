from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from time import sleep


class OffPlanPage(BasePage):
    SALES_STATUS = (By.CSS_SELECTOR, "select#Location-2")
    PROJECT_NAMES = (By.CSS_SELECTOR, "div[wized='projectName']")

    def select_sales_status(self, option):
        dropdown = self.find_element(*self.SALES_STATUS)
        select = Select(dropdown)
        select.select_by_value(option)

    def verify_contains_option(self, option):
        product_filter_locator = (By.XPATH, f"//div[@wized='projectStatus' and contains(text(), '{option}')]")
        product_filter_items = [elem.text for elem in self.find_elements(*product_filter_locator)]
        project_names = [elem.text for elem in self.find_elements(*self.PROJECT_NAMES)]
        print(product_filter_items, len(product_filter_items), sep='\n')
        print(project_names, len(project_names), sep='\n')
        assert len(product_filter_items) == len(project_names) and product_filter_items.count(option) == len(product_filter_items),\
            f"Not all options are displayed correctly for '{option}'"
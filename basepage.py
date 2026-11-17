class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def send_keys(self,locator,data):
        ele = self.driver.find_element(*locator)
        ele.clear()
        ele.send_keys(data)

    def click(self,locator):
        ele1 = self.driver.find_element(*locator)
        ele1.click()


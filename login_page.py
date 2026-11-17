from basepage import BasePage
from selenium.webdriver.common.by import By

class Login(BasePage):

    User_Name = (By.ID,"name")
    User_Email = (By.ID,"email")
    User_Phone = (By.ID, "phone")


    def user_enter_name(self,data):
        self.send_keys(self.User_Name,data)

    def user_enter_email(self,data):
        self.send_keys(self.User_Email,data)

    def user_enter_phone(self,data):
        self.send_keys(self.User_Phone,data)

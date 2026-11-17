from login_page import Login
import pytest
import allure
from selenium.webdriver.common.by import By


class TestLogin:
    @allure.feature("Login")
    @allure.story("Username")
    @allure.title("Verify username with {user_name}")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("user_name",["Mithun","Mahesh","king"])
    def test_enter_user_name(self,user_name,set_up):
        login = Login(set_up)
        login.user_enter_name(user_name)

    @allure.feature("Login")
    @allure.story("Email")
    @allure.title("Verify Email with {user_email}")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("user_email", ["Mithun123@gmail.com", "Mahesh321@gmail.com", "king908@gmail.com"])
    def test_enter_user_email(self,user_email,set_up):
        login = Login(set_up)
        login.user_enter_email(user_email)

    @allure.feature("Login")
    @allure.story("Phone")
    @allure.title("Verify Phone with {user_phone}")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("user_phone", ["7890349023", "8901234890"])
    def test_enter_user_phone(self,user_phone,set_up):
        login = Login(set_up)
        login.user_enter_phone(user_phone)


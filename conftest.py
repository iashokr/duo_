import pytest
from selenium import webdriver


@pytest.fixture
def set_up():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    yield driver
    driver.quit()
x
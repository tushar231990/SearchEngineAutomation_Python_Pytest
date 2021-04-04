import pytest
from selenium import webdriver
from Config.config import TestData


@pytest.fixture(params=["Chrome","Firefox"],scope="class")
def init_driver(request):
    if request.param == "Chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.ChromeExecutablePath)
    if request.param == "Firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FirefoxExecutablePath)
    request.cls.driver = web_driver
    web_driver.delete_all_cookies()
    web_driver.maximize_window()
    yield
    web_driver.close()
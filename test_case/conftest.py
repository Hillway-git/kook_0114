import pytest
from selenium import webdriver



# @pytest.fixture(scope="session")
# def driver():
#     # 打开浏览器
#     driver = webdriver.Chrome("../chrome_driver_v79/chromedriver.exe")
#     # 窗口最大化
#     driver.maximize_window()
#     yield driver     D:\softwaredata\ui_auto\chrome_driver_v79\chromedriver.exe
#     # 关闭浏览器
#     driver.quit()
from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9111")
    driver = webdriver.Chrome("../chrome_driver_v79/chromedriver.exe", chrome_options=chrome_options)
    driver.implicitly_wait(10)
    return driver
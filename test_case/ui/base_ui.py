#!/usr/bin/env python
# -*- coding:utf-8 -*-




# 把selenium常用操作封装到BaseUI这个类中，我们再写用例的时候，就可以简化代码量了。
from selenium import webdriver

from test_case.conf.config import WEB_DRIVER


class BaseUI():

    def start_browser(self):
        driver = webdriver.Chrome(WEB_DRIVER)
        # 窗口最大化
        driver.maximize_window()
        driver.implicitly_wait(20) # 隐式等待
        self.driver = driver
    def quit(self):
        self.driver.quit()
    def get(self,url):
        self.driver.get(url)
    def click(self,xpath):
        el = self.driver.find_element_by_xpath(xpath)
        el.click()
    def send_keys(self,xpath,text):
        el = self.driver.find_element_by_xpath(xpath)
        el.clear()
        el.send_keys(text)
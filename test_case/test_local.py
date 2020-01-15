import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test_case.conftest import driver


def test_xpath(driver):
    eles=driver.find_elements_by_xpath("//input")
    print(type(eles))
    for e in eles:
        e.send_keys("hh123")
        time.sleep(2)

def test_xpath(driver):
    driver.refresh()
    eles=driver.find_elements(By.XPATH,"//input")
    print(type(eles))
    for e in eles:
        e.send_keys("520")
        time.sleep(2)

def test_input(driver):
    name=driver.find_elements_by_xpath("//input")
    name.clear()
    for i in name:
        i.clear()
        i.send_keys("我我123")
        time.sleep(1)


def test_radio(driver):
    driver.find_element_by_xpath('//label//span[text()="广州"]').click()


def test_ui(driver):
    driver.get('http://ui.yansl.com/#/select')


def test_select1(driver):
    sel=driver.find_element_by_tag_name("select")
    #Select 是一个类，封装了所有的对下拉框的一些操作的方法
    s=Select(sel)
    #调用这个类
    s.select_by_visible_text("小米")
    time.sleep(1)
    s.select_by_value("huawei")
    time.sleep(1)
    s.select_by_index(3)

def test_select2(driver):
    driver.find_element_by_xpath("//select/option[text()='华为']").click()
    time.sleep(3)

def test_hover(driver):
    zhinan=driver.find_element_by_xpath('//ul//li//span[@class="el-cascader-node__label"][last()]')
    action=ActionChains(driver)
    action.move_to_element(zhinan).perform()
    action.perform()
    time.sleep(1)

def test_splider(driver):
    splider=driver.find_element_by_xpath('''(//div//div[@class="el-tooltip el-slider__button"])[last()-5]''')
    action=ActionChains(driver)
    action.drag_and_drop_by_offset(splider,-100,0).perform()
    time.sleep(2)
    action.reset_actions()
    action.drag_and_drop_by_offset(splider, 100, 0).perform()


def test_splider2(driver):
    splider2=driver.find_element_by_xpath('''(//div//div[@class="el-tooltip el-slider__button"])[last()]''')
    action=ActionChains(driver)
    action.drag_and_drop_by_offset(splider2,0,-100).perform()
    time.sleep(2)

def test_date(driver):
    da=driver.find_element_by_xpath('//div//input[@placeholder="选择时间"]')
    print(type(da))
    da.clear()
    da.send_keys("15:41")

def test_date2(driver):
    da2=driver.find_element_by_xpath('//div//input[@placeholder="选择日期"]')
    print(type(da2))
    da2.clear()
    da2.send_keys("2020-01-22")

def test_date3(driver):
    da3=driver.find_element_by_xpath('//div//input[@placeholder="选择一个或多个日期"]')
    print(type(da3))
    da3.clear()
    da3.send_keys("2020-01-05,2020-01-29")

import time
from lib2to3.pgen2 import driver

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


def test_start(driver):
    time.sleep(6)
    driver.get("http://www.baidu.com")
    time.sleep(6)
    driver.get("http://www.taobao.com")
    time.sleep(6)
    driver.get("http://www.jd.com")
    time.sleep(6)
    driver.back()
    time.sleep(6)
    driver.forward()
    time.sleep(6)
    driver.refresh()
    time.sleep(6)

def test_debugger(driver):
    time.sleep(2)
    driver.find_element_by_name("t2").send_keys("llove1")
    time.sleep(1)

def test_xpath(driver):
    eles = driver.find_elements_by_xpath("//input")
    print(type(eles))
    for e in eles:
        e.send_keys("happy")
        time.sleep(1)

def test_radio(driver):
    driver.find_element_by_xpath('//label[@role="radio"]//span[text()="广州"]').click()

def test_select_1(driver):
    sel = driver.find_element_by_tag_name("select")
    s =Select(sel)
    s.select_by_visible_text("小米")
    time.sleep(1)
    s.select_by_value("huawei")
    time.sleep(1)

def test_hover(driver):
    time.sleep(2)
    zhi_nan =driver.find_element_by_xpath('(//span[text()="指南"])[last()]')
    action = ActionChains(driver)
    action.move_to_element(zhi_nan)
    action.perform()
    time.sleep(2)

def test_splider(driver):
    time.sleep(1)
    splider = driver.find_element_by_xpath('''
    //label[text()="普通滑块"]/../div//div[@class="el-tooltip el-slider__button"]
        ''')
    action =ActionChains(driver)
    action.drag_and_drop_by_offset(splider,100,0).perform()
    action.reset_actions()
    time.sleep(2)
    action.drag_and_drop_by_offset(splider,-100,0).perform()
    action.reset_actions()



def test_splider2(driver):
    time.sleep(1)
    splider = driver.find_element_by_xpath('''
    //label[text()="竖向选择"]/../div//div[@class="el-tooltip el-slider__button"]
        ''')
    action =ActionChains(driver)
    action.drag_and_drop_by_offset(splider,0,90).perform()
    action.reset_actions()
    time.sleep(2)
    action.drag_and_drop_by_offset(splider,0,-90).perform()
    action.reset_actions()

def test_data(driver):
    da = driver.find_element_by_xpath(
        """//label[text()="固定时间"]/../div//input
        """)
    da.send_keys()

def test_date(driver):
    da=driver.find_element_by_xpath('//label[text()=("单个日期")]/../div//input')
    da.send_keys("2020-01-27")
    time.sleep(3)

# 1、id属性定位
from time import sleep, time


def test_baidu(driver):
    # id属性定位
    element_selector = driver.find_element_by_id("kw")
    element_selector.send_keys("果芽软件")
    # 返回WebElement类型
    print(type(element_selector))
    time.sleep(1)
# 2、 name属性定位

def test_baidu(driver):
    # name属性定位
    element_selector = driver.find_element_by_name("wd")
    element_selector.send_keys("果芽软件")
    # 返回WebElement类型
    print(type(element_selector))
    time.sleep(1)
# 3、class属性定位

def test_baidu(driver):
    # class_name属性定位
    element_classname = driver.find_element_by_class_name("s_ipt")
    element_classname.send_keys("果芽软件")
    # 返回WebElement类型
    print(type(element_classname))
    time.sleep(1)
# 4、tag name标签名称定位

def test_baidu(driver):
    # tag name标签名称定位
    element_tagname = driver.find_element_by_tag_name("input")
    # 返回WebElement类型
    print(type(element_tagname))
    time.sleep(1)
# 5、link text通过超链接的完整文本定位

def test_baidu(driver):
    # link text通过超链接的完整文本定位
    element_linktext = driver.find_element_by_link_text("学术")
    element_linktext.click()
    # 返回WebElement类型
    print(type(element_linktext))
    time.sleep(1)
# 6、partial link text通过超链接的部分文本定位

def test_baidu(driver):
    # partial link text通过超链接的部分文本定位
    element_partial_linktext = driver.find_element_by_partial_link_text("百度")
    element_partial_linktext.click()
    # 返回WebElement类型
    print(type(element_partial_linktext))
    time.sleep(1)
# 7、xpath 通过xpath定位
# xpath 绝对路径定位

def test_baidu(driver):
    # partial link text通过超链接的部分文本定位
    element_xpath_j = driver.find_element_by_xpath('//*[@id="form"]/span[1]/span')
    element_xpath_j.click()
    # 返回WebElement类型
    print(type(element_xpath_j))
    time.sleep(1)
# xpath 相对路径定位

def test_baidu(driver):
    # 定位多个xpath,用find_elements_by_xpath 循环遍历输入
    # 返回的是一个列表
    element_xpath = driver.find_elements_by_xpath("//input")
    for i in element_xpath:
        i.send_keys("果芽软件")
        time.sleep(1)
    # 返回的是一串列表，里面包含了定位到的每个xpath元素
    print(type(element_xpath))
    time.sleep(1)
# 8、css selector定位

def test_baidu(driver):
    # css selector 方式定位
    element_selector = driver.find_element_by_css_selector('[id="kw"]')
    element_selector.send_keys("果芽软件")
    # 返回WebElement类型
    print(type(element_selector))
    time.sleep(1)
from time import sleep

import autoit as autoit


def test_xpath(driver):
    eles = driver.find_elements_by_name("//input")
    print(type(eles))
    for e in eles:
        e.send_keys("bbts")
        sleep(1)

# def test_time(driver):
#     time = "var xpath = "//input[@placeholder='任意时间']" ;var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute("value" ,"19:56:30");"
#     driver.execute_script(time)

def test_upload_file1(driver):
    file = driver.find_element_by_xpath("//label[text()='原始上传']/..//div//input")
    file.send_keys("C:\\Users\\admin\\Desktop\\hillway.html")


def test_upload_file2(driver):
    file = driver.find_element_by_xpath("//label[text()='点击上传']/..//div//span").click()
    sleep(3)
    autoit.control_set_text("打开", "Edit1", "C:\\Users\\admin\\Desktop\\hillway.png")
    sleep(3)
    autoit.control_click("打开", "Button1")
    pass

def test_expanded(driver):
    yi_ji = driver.find_element_by_xpath('//label[text()="普通树"]/..//div//span[text()="一级 1"]')
    yi_class =yi_ji.get_attribute("class")
    if "expanded" in yi_class:
        pass
    else:
        yi_ji.click()
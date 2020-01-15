import time


#def test_start(driver):
   # driver.get("http://ui.yansl.com/#/input")
    #time.sleep(1)
    # driver.refresh()
    # driver.get("http://www.jd.com")
    # time.sleep(1)
    # driver.get("http://www.taobao.com")
    # time.sleep(1)
    # driver.back()
    # time.sleep(1)
    # driver.forward()
    # time.sleep(1)


def test_debugger(driver):
    #driver.get("http://ui.yansl.com/#/input")
    driver.find_element_by_name("t1").send_keys("hhhhh")

import time


def test_case(driver):
    driver.find_element_by_xpath('//div//span[text()="region1"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//div//span[text()="zone2"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//div//span[text()="zone4"]').click()





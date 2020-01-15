import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_input_1(driver):
    one =driver.find_elements_by_xpath('//label[text()="纯输入框"]/..//input')
    print(type(one))
    for o in one:
        o.send_keys("123456")



def test_keys(driver):
    time.sleep(2)
    a=driver.find_element_by_tag_name("a")
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(a).key_up(Keys.CONTROL).perform()


def test_windwos(driver):
    handles=driver.window_handles
    for h in handles:
        driver.switch_to.window(h)
        time.sleep(2)
        if "淘宝" in driver.title:
            break

def test_prompt(driver):
    time.sleep(2)
    alert =driver.switch_to_alert()
    print(alert.text)
    alert.accept()
    alert.dismiss()
    alert.send_keys("nvhjsdn")


def test_frame(driver):
    frame =driver.find_element_by_xpath('(//iframe[contains(@id,"tinymce")])[1]')
    driver.switch_to.frame(frame)
    body =driver.find_element_by_id("tinymce")
    body.send_keys("ajsdbnshb")
    driver.switch_to.parent_frame()
    driver.find_element_by_xpath('//div[@class="el-upload el-upload--picture-card"]//i[@class="el-icon-plus"]').click()


def test_in_wait(driver):
    time.sleep(2)
    driver.find_element_by_xpath('//label[text()="下拉框2"]/..//input').click()
    op = driver.find_element_by_xpath('(//ul)[last()]//span[text()="双皮奶"]')
    action = ActionChains(driver)
    action.move_to_element(op).click().perform()

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def test_xian_wait(driver):
    WebDriverWait(driver, 60, 0.5).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="code-btn"]')))
    driver.find_element_by_xpath('//button[@class="code-btn"]').click()
    
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from tools.report.decorators_tool import shot
from tools.os import os_tool


class BaseUI:

    original_window = None

    def __init__(self, browser='chrome'):
        self.driver = None
        if browser == "firefox" or browser == "ff":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            driver_path = os_tool.get_root_path()+ "chrome_driver/chromedriver.exe"
            self.driver = webdriver.Chrome(driver_path)
            self.driver.maximize_window()
            self.driver.implicitly_wait(8)
        elif browser == "internet explorer" or browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == "opera":
            self.driver = webdriver.Opera()
        elif browser == "chrome_headless":
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            self.driver = webdriver.Chrome('../../chrome_driver/chromedriver.exe',chrome_options=chrome_options)
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        else:
            raise NameError(
                "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'edge', 'chrome' or 'chrome_headless'." % browser)

        self.location_type_dict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "css_selector": By.CSS_SELECTOR,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }

    @shot
    def max_window(self):
        """
        Set browser window maximized.
        Usage:
        driver.max_window()
        """
        self.driver.maximize_window()

    @shot
    def set_window(self, wide, high):
        """
        Set browser window wide and high.
        Usage:
        driver.set_window(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def close(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.
        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.
        Usage:
        driver.quit()
        """
        self.driver.quit()

    @shot
    def open(self, url):
        """
        open url.
        Usage:
        driver.open("https://www.baidu.com")
        """
        self.driver.get(url)

    @shot
    def forward(self):
        self.driver.forward()

    @shot
    def back(self):
        self.driver.back()

    @shot
    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        """
        Get window title.
        Usage:
        driver.get_title()
        """
        return self.driver.title

    def get_url(self):
        """
        Get the URL address of the current page.
        Usage:
        driver.get_url()
        """
        return self.driver.current_url

    def get_element(self, locator):
        """
        Judge element positioning way, and returns the element.
        """
        if "=>" not in locator:
            by = "xpath"
            value = locator
        else:
            by = locator.split("=>")[0].strip()
            value = locator.split("=>")[1].strip()
            if by == "" or value == "":
                raise NameError(
                    "Grammatical errors, reference: 'id=>useranme'.")

        time_out_error = "定位元素超时，请尝试其他定位方式"
        if by == "id":
            req = self.wait_element((By.ID, value))
            if req is True:
                element = self.driver.find_element_by_id(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "name":
            req = self.wait_element((By.NAME, value))
            if req is True:
                element = self.driver.find_element_by_name(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "class":
            req = self.wait_element((By.CLASS_NAME, value))
            if req is True:
                element = self.driver.find_element_by_class_name(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "link_text":
            req = self.wait_element((By.LINK_TEXT, value))
            if req is True:
                element = self.driver.find_element_by_link_text(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "xpath":
            req = self.wait_element((By.XPATH, value))
            if req is True:
                element = self.driver.find_element_by_xpath(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "css":
            req = self.wait_element((By.CSS_SELECTOR, value))
            if req is True:
                element = self.driver.find_element_by_css_selector(value)
            else:
                raise TimeoutException(time_out_error)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def wait_element(self, el):
        """
        Waiting for an element to display.
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(el)
            )
        except TimeoutException:
            return False
        else:
            return True

    @shot
    def send_keys(self, locator, text):
        """
        Operation input box.
        Usage:
        driver.type("css=>#el","selenium")
        """
        el = self.get_element(locator)
        el.send_keys(text)

    @shot
    def clear(self, locator):
        """
        Clear the contents of the input box.
        Usage:
        driver.clear("locator=>#el")
        """
        el = self.get_element(locator)
        el.clear()

    @shot
    def click(self, locator):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..
        Usage:
        driver.click("locator=>#el")
        """
        el = self.get_element(locator)
        el.click()

    @shot
    def click_link(self, text):
        """
        Click the element by the link text
        Usage:
        driver.click_text("新闻")
        """
        self.driver.find_element_by_partial_link_text(text).click()

    @shot
    def right_click(self, locator):
        """
        Right click element.
        Usage:
        driver.right_click("css=>#el")
        """
        el = self.get_element(locator)
        ActionChains(self.driver).context_click(el).perform()

    @shot
    def double_click(self, locator):
        """
        Double click element.
        Usage:
        driver.double_click("css=>#el")
        """
        el = self.get_element(locator)
        ActionChains(self.driver).double_click(el).perform()

    @shot
    def move_to_element(self, locator):
        """
        Mouse over the element.
        Usage:
        driver.move_to_element("css=>#el")
        """
        el = self.get_element(locator)
        ActionChains(self.driver).move_to_element(el).perform()

    @shot
    def drag_and_drop(self, el_locator, ta_locator):
        """
        Drags an element a certain distance and then drops it.
        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        """
        element = self.get_element(el_locator)
        target = self.get_element(ta_locator)
        ActionChains(self.driver).drag_and_drop(element, target).perform()



    @shot
    def submit(self, locator):
        """
        Submit the specified form.
        Usage:
        driver.submit("css=>#el")
        """
        el = self.get_element(locator)
        el.submit()


    @shot
    def js(self, script):
        """
        Execute JavaScript scripts.
        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def get_attribute(self, locator, attribute):
        """
        Gets the value of an element attribute.
        Usage:
        driver.get_attribute("locator=>#el","type")
        """
        el = self.get_element(locator)
        return el.get_attribute(attribute)

    def get_text(self, locator):
        """
        Get element text information.
        Usage:
        driver.get_text("locator=>#el")
        """
        el = self.get_element(locator)
        return el.text

    def get_display(self, locator):
        """
        Gets the element to display,The return result is true or false.
        Usage:
        driver.get_display("locator=>#el")
        """
        el = self.get_element(locator)
        return el.is_displayed()


    def get_alert_text(self):
        """
        Gets the text of the Alert.
        Usage:
        driver.get_alert_text()
        """
        return self.driver.switch_to.alert.text

    @shot
    def alert_accept(self):
        """
        Accept warning box.
        Usage:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    @shot
    def alert_dismiss(self):
        """
        Dismisses the alert available.
        Usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    @shot
    def switch_to_frame(self, css):
        """
        Switch to the specified frame.
        Usage:
        driver.switch_to_frame("css=>#el")
        """
        iframe_el = self.get_element(css)
        self.driver.switch_to.frame(iframe_el)

    @shot
    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    @shot
    def switch_to_window(self, locator):
        """
        Open the new window and switch the handle to the newly opened window.
        Usage:
        driver.open_new_window("link_text=>注册")
        """
        original_window = self.driver.current_window_handle
        el = self.get_element(locator)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)

    def screenshot(self, file_path):
        """
        Saves a screenshot of the current window to a PNG image file.
        Usage:
        driver.get_screenshot('/Screenshots/foo.png')
        """
        self.driver.get_screenshot_as_file(file_path)

    @shot
    def select_by_value(self, locator, value):
        el = self.get_element(locator)
        Select(el).select_by_value(value)

    @shot
    def select_by_index(self, locator, value):
        el = self.get_element(locator)
        Select(el).select_by_index(value)

    @shot
    def select_by_text(self, locator, value):
        el = self.get_element(locator)
        Select(el).select_by_visible_text(value)

    def sleep(self, sec):
        time.sleep(sec)

    def wait_time(self, secs):
        """
        Implicitly wait.All elements on the page.
        Usage:
        driver.wait(10)
        """
        self.driver.implicitly_wait(secs)

    # 显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象
    def wait_util_presence(self,locat_type,locate_value,secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                element = WebDriverWait(self.driver, secs).until(
                            EC.presence_of_element_located((
                                self.location_type_dict[locat_type], locate_value)))
                return element
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    # 显示等待页面元素的出现
    def wait_util_visibility(self, locat_type, locate_value, secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                element = WebDriverWait(self.driver, secs).until(
                    EC.visibility_of_element_located((
                        self.location_type_dict[locat_type], locate_value)))
                return element
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    # 显示等待页面元素的出现
    def wait_util_not_visibility(self, locat_type, locate_value, secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                element = WebDriverWait(self.driver, secs).until(
                    EC.invisibility_of_element_located((
                        self.location_type_dict[locat_type], locate_value)))
                return element
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    '''判断某个元素中是否可见并且是enable的，代表可点击'''
    def wait_util_clickable(self, locat_type, locate_value, secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                element = WebDriverWait(self.driver, secs).until(
                    EC.element_to_be_clickable((
                        self.location_type_dict[locat_type], locate_value)))
                return element
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    '''判断某个元素是否被选中了,一般用在下拉列表'''
    def wait_util_selected(self, locat_type, locate_value, secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                element = WebDriverWait(self.driver, secs).until(
                    EC.element_to_be_selected((
                        self.location_type_dict[locat_type], locate_value)))
                return element
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    def wait_util_text(self, locat_type, locate_value, secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                is_true = WebDriverWait(self.driver, secs).until(
                    EC.text_to_be_present_in_element((
                        self.location_type_dict[locat_type], locate_value)))
                return is_true
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e
    '''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''
    def wait_util_at_lest_one(self, locat_type, locate_value, secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                items = WebDriverWait(self.driver, secs).until(
                    EC.presence_of_all_elements_located((
                        self.location_type_dict[locat_type], locate_value)))
                return items
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e



    # 显示等待页面为指定title
    def wait_util_title_is(self, locat_type, locate_value, secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                is_true = WebDriverWait(self.driver, secs).until(
                    EC.title_is((
                        self.location_type_dict[locat_type], locate_value)))
                return is_true
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    # 显示等待页面title包含指定内容
    def wait_util_title_contains(self, locat_type, locate_value, secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                is_true = WebDriverWait(self.driver, secs).until(
                    EC.title_contains((
                        self.location_type_dict[locat_type], locate_value)))
                return is_true
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    # 显示等待页面title包含指定内容
    def wait_util_title_contains(self, locat_type, locate_value, secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                is_true = WebDriverWait(self.driver, secs).until(
                    EC.title_contains((
                        self.location_type_dict[locat_type], locate_value)))
                return is_true
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    '''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
    def wait_util_alert_present(self, locat_type, locate_value, secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                element = WebDriverWait(self.driver, secs).until(
                    EC.alert_is_present((
                        self.location_type_dict[locat_type], locate_value)))
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    # 检查frame是否存在，存在则切换进去
    def wait_util_frame_available(self, locat_type, locate_value, secs=10):
        try:
            if locat_type.lower() in self.locationTypeDict:
                element = WebDriverWait(self.driver, secs).until(
                    EC.frame_to_be_available_and_switch_to_it((
                        self.location_type_dict[locat_type], locate_value)))
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

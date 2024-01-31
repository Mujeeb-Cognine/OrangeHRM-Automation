import os
import win32clipboard
import inspect
import logging
import time
import math

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from OrangeHRMData.Enums import ActionKeys
from OrangeHRMData.Strings import Strings
from OrangeHRMData.Constants import Constants
from _Wrapper.DefaultLogger import DefaultLog
from _Wrapper.DriverInitialization import DriverInitialization


class BaseClass(DriverInitialization):

    logger_name = None  # Class attribute to store the logger name
    _base_url = None  # Class variable to store the base_url
    logger = DefaultLog.get(__name__)

    @classmethod
    def setup(cls):
        cls.s = Strings()
        cls.const = Constants()

    @classmethod
    def set_base_url(cls, url):
        cls._base_url = url
        cls.logger.info("set_base_url got set")

    @classmethod
    def get_base_url(cls):
        return cls._base_url

    @classmethod
    def get_bearer_token(cls):
        return os.getenv("bearer")

    @classmethod
    def navigate_to_url(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.get(cls.get_base_url())
        cls.driver.maximize_window()

    @classmethod
    def find_element(cls, element_locator, selector="xpath"):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        if selector == "xpath":
            return cls.find_element_by_xpath(element_locator)
        if selector == "id":
            return cls.find_element_by_id(element_locator)
        if selector == "link text":
            return cls.find_element_by_link_text(element_locator)
        if selector == "partial link text":
            return cls.find_element_by_partial_link_text(element_locator)
        if selector == "name":
            return cls.find_element_by_name(element_locator)
        if selector == "tag name":
            return cls.find_element_by_tag_name(element_locator)
        if selector == "class name":
            return cls.find_element_by_class_name(element_locator)
        if selector == "css selector":
            return cls.find_element_by_css_selector(element_locator)

    @classmethod
    def find_element_by_id(cls, ID):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_element(By.ID, ID)

    @classmethod
    def find_element_by_xpath(cls, Xpath):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_element(By.XPATH, Xpath)

    @classmethod
    def find_element_by_class_name(cls, ClassName):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_element(By.CLASS_NAME, ClassName)

    @classmethod
    def find_element_by_name(cls, Name):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_element(By.NAME, Name)

    @classmethod
    def find_element_by_tag_name(cls, TagName):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_element(By.TAG_NAME, TagName)

    @classmethod
    def find_element_by_css_selector(cls, CssSelector):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_element(By.CSS_SELECTOR, CssSelector)

    @classmethod
    def find_element_by_link_text(cls, LinkText):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_element(By.LINK_TEXT, LinkText)

    @classmethod
    def find_element_by_partial_link_text(cls, PartialLinkText):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_element(By.PARTIAL_LINK_TEXT, PartialLinkText)

    @classmethod
    def find_elements(cls, elements_locator, selector='xpath'):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        if selector == "xpath":
            return cls.find_elements_by_xpath(elements_locator)
        if selector == "id":
            return cls.find_elements_by_id(elements_locator)
        if selector == "link text":
            return cls.find_elements_by_link_text(elements_locator)
        if selector == "partial link text":
            return cls.find_elements_by_partial_link_text(elements_locator)
        if selector == "name":
            return cls.find_elements_by_name(elements_locator)
        if selector == "tag name":
            return cls.find_elements_by_tag_name(elements_locator)
        if selector == "class name":
            return cls.find_elements_by_class_name(elements_locator)
        if selector == "css selector":
            return cls.find_elements_by_css_selector(elements_locator)

    @classmethod
    def find_elements_by_id(cls, ID):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_elements(By.ID, ID)

    @classmethod
    def find_elements_by_xpath(cls, Xpath):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_elements(By.XPATH, Xpath)

    @classmethod
    def find_elements_by_class_name(cls, ClassName):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_elements(By.CLASS_NAME, ClassName)

    @classmethod
    def find_elements_by_name(cls, Name):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_elements(By.NAME, Name)

    @classmethod
    def find_elements_by_tag_name(cls, TagName):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_elements(By.TAG_NAME, TagName)

    @classmethod
    def find_elements_by_css_selector(cls, CssSelector):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_elements(By.CSS_SELECTOR, CssSelector)

    @classmethod
    def find_elements_by_link_text(cls, LinkText):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_elements(By.LINK_TEXT, LinkText)

    @classmethod
    def find_elements_by_partial_link_text(cls, PartialLinkText):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_elements(By.PARTIAL_LINK_TEXT, PartialLinkText)

    @classmethod
    def click_element(cls, element_locator, selector="xpath"):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        element = cls.find_element(element_locator)
        element.click()

    @classmethod
    def send_keys_to_element(cls, element_locator, keys):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        element = cls.find_element(element_locator)
        element.send_keys(keys)

    @classmethod
    def wait_for_element_presence(cls, element_locator, timeout=Constants.short_live_throttle, selector="xpath"):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        if selector == "xpath":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, element_locator)))
        if selector == "id":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_locator)))
        if selector == "link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_element_located((By.LINK_TEXT, element_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element_locator)))
        if selector == "name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_element_located((By.NAME, element_locator)))
        if selector == "tag name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, element_locator)))
        if selector == "class name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, element_locator)))
        if selector == "css selector":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, element_locator)))

    @classmethod
    def wait_for_all_elements_presence(cls, elements_locator, timeout=Constants.short_live_throttle, selector="xpath"):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        if selector == "xpath":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, elements_locator)))
        if selector == "id":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_all_elements_located((By.ID, elements_locator)))
        if selector == "link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_all_elements_located((By.LINK_TEXT, elements_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, elements_locator)))
        if selector == "name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_all_elements_located((By.NAME, elements_locator)))
        if selector == "tag name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, elements_locator)))
        if selector == "class name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, elements_locator)))
        if selector == "css selector":
            return WebDriverWait(cls.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, elements_locator)))

    @classmethod
    def go_back(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.back()

    @classmethod
    def go_forward(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.forward()

    @classmethod
    def refresh_page(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.refresh()

    @classmethod
    def take_screenshot(cls, screenshot_name):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")

        try:
            # Save the screenshot in the sub-folder with a timestamped filename
            cls.driver.save_screenshot(screenshot_name)

            print(f"Screenshot saved with name: {screenshot_name}")
        except Exception as e:
            print(f"Failed to take screenshot: {e}")

    @classmethod
    def get_screenshot_as_base64(cls):
        return cls.driver.get_screenshot_as_base64()

    @classmethod
    def close_browser(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.close()

    @classmethod
    def quit_browser(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.quit()

    @classmethod
    def get_current_url(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.current_url

    @classmethod
    def get_page_title(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.title

    @classmethod
    def implicitly_wait(cls, seconds):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.implicitly_wait(seconds)

    @classmethod
    def wait_for_element_clickable(cls, element_locator, timeout=Constants.short_live_throttle, selector="xpath"):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        if selector == "xpath":
            return WebDriverWait(cls.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, element_locator)))
        if selector == "id":
            return WebDriverWait(cls.driver, timeout).until(
                EC.element_to_be_clickable((By.ID, element_locator)))
        if selector == "link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.element_to_be_clickable((By.LINK_TEXT, element_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, element_locator)))
        if selector == "name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.element_to_be_clickable((By.NAME, element_locator)))
        if selector == "tag name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.element_to_be_clickable((By.TAG_NAME, element_locator)))
        if selector == "class name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.element_to_be_clickable((By.CLASS_NAME, element_locator)))
        if selector == "css selector":
            return WebDriverWait(cls.driver, timeout).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, element_locator)))

    @classmethod
    def wait_for_visibility_of_element(cls, element_locator, timeout=Constants.short_live_throttle, selector="xpath"):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        if selector == "xpath":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, element_locator)))
        if selector == "id":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_element_located((By.ID, element_locator)))
        if selector == "link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_element_located((By.LINK_TEXT, element_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, element_locator)))
        if selector == "name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_element_located((By.NAME, element_locator)))
        if selector == "tag name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_element_located((By.TAG_NAME, element_locator)))
        if selector == "class name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, element_locator)))
        if selector == "css selector":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, element_locator)))

    @classmethod
    def wait_for_visibility_of_all_elements(cls, elements_locator, timeout=Constants.short_live_throttle,
                                            selector="xpath"):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        if selector == "xpath":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.XPATH, elements_locator)))
        if selector == "id":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.ID, elements_locator)))
        if selector == "link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.LINK_TEXT, elements_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.PARTIAL_LINK_TEXT, elements_locator)))
        if selector == "name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.NAME, elements_locator)))
        if selector == "tag name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.TAG_NAME, elements_locator)))
        if selector == "class name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, elements_locator)))
        if selector == "css selector":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, elements_locator)))

    @classmethod
    def wait_for_visibility_of_any_elements(cls, elements_locator, timeout=Constants.short_live_throttle,
                                            selector="xpath"):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        if selector == "xpath":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_any_elements_located((By.XPATH, elements_locator)))
        if selector == "id":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_any_elements_located((By.ID, elements_locator)))
        if selector == "link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_any_elements_located((By.LINK_TEXT, elements_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_any_elements_located((By.PARTIAL_LINK_TEXT, elements_locator)))
        if selector == "name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_any_elements_located((By.NAME, elements_locator)))
        if selector == "tag name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_any_elements_located((By.TAG_NAME, elements_locator)))
        if selector == "class name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_any_elements_located((By.CLASS_NAME, elements_locator)))
        if selector == "css selector":
            return WebDriverWait(cls.driver, timeout).until(
                EC.visibility_of_any_elements_located((By.CSS_SELECTOR, elements_locator)))

    @classmethod
    def wait_for_invisibility_of_element(cls, element_locator, timeout=Constants.short_live_throttle, selector="xpath"):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        if selector == "xpath":
            return WebDriverWait(cls.driver, timeout).until(
                EC.invisibility_of_element_located((By.XPATH, element_locator)))
        if selector == "id":
            return WebDriverWait(cls.driver, timeout).until(
                EC.invisibility_of_element_located((By.ID, element_locator)))
        if selector == "link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.invisibility_of_element_located((By.LINK_TEXT, element_locator)))
        if selector == "partial link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.invisibility_of_element_located((By.PARTIAL_LINK_TEXT, element_locator)))
        if selector == "name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.invisibility_of_element_located((By.NAME, element_locator)))
        if selector == "tag name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.invisibility_of_element_located((By.TAG_NAME, element_locator)))
        if selector == "class name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, element_locator)))
        if selector == "css selector":
            return WebDriverWait(cls.driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, element_locator)))

    @classmethod
    def wait_for_text_to_be_present_in_element(cls, element_locator, text, timeout=Constants.short_live_throttle,
                                               selector="xpath"):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        if selector == "xpath":
            return WebDriverWait(cls.driver, timeout).until(
                EC.text_to_be_present_in_element((By.XPATH, element_locator), text))
        if selector == "id":
            return WebDriverWait(cls.driver, timeout).until(
                EC.text_to_be_present_in_element((By.ID, element_locator), text))
        if selector == "link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.text_to_be_present_in_element((By.LINK_TEXT, element_locator), text))
        if selector == "partial link text":
            return WebDriverWait(cls.driver, timeout).until(
                EC.text_to_be_present_in_element((By.PARTIAL_LINK_TEXT, element_locator), text))
        if selector == "name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.text_to_be_present_in_element((By.NAME, element_locator), text))
        if selector == "tag name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, element_locator), text))
        if selector == "class name":
            return WebDriverWait(cls.driver, timeout).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, element_locator), text))
        if selector == "css selector":
            return WebDriverWait(cls.driver, timeout).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, element_locator), text))

    @classmethod
    def is_element_displayed(cls, element_locator):
        element = cls.find_element(element_locator)
        element.is_displayed()

    @classmethod
    def is_element_not_displayed(cls, element_locator):
        try:
            element = cls.find_element(element_locator)
            return not element.is_displayed()
        except NoSuchElementException:
            # Element not found, consider it as not displayed
            return True

    @classmethod
    def is_element_enabled(cls, element_locator):
        element = cls.find_element(element_locator)
        element.is_enabled()

    @classmethod
    def is_element_not_enabled(cls, element_locator):
        try:
            element = cls.find_element(element_locator)
            return not element.is_enabled()
        except NoSuchElementException:
            # Element not found, consider it as not enabled
            return True

    @classmethod
    def clear_element(cls, element_locator):
        element = cls.find_element(element_locator)
        element.clear()

    @classmethod
    def get_text(cls, element_locator):
        element = cls.find_element(element_locator)
        return element.text

    @classmethod
    def get_attribute(cls, element_locator, attribute_name):
        element = cls.find_element(element_locator)
        return element.get_attribute(attribute_name)

    @classmethod
    def perform_hover(cls, element_locator):
        element = cls.find_element(element_locator)
        ActionChains(cls.driver).move_to_element(element).perform()

    @classmethod
    def press_key(cls, key):
        ActionChains(cls.driver).send_keys(key).perform()

    @classmethod
    def press_enter(cls):
        cls.press_key(ActionKeys.ENTER)

    @classmethod
    def press_tab(cls):
        cls.press_key(ActionKeys.TAB)

    @classmethod
    def switch_to_frame(cls, element_locator):
        frame = cls.find_element(element_locator)
        cls.driver.switch_to.frame(frame)

    @classmethod
    def switch_to_default_content(cls):
        cls.driver.switch_to.default_content()

    @classmethod
    def get_current_window_handle(cls):
        return cls.driver.current_window_handle

    @classmethod
    def accept_alert(cls):
        Alert(cls.driver).accept()

    @classmethod
    def dismiss_alert(cls):
        Alert(cls.driver).dismiss()

    @classmethod
    def get_alert_text(cls):
        return Alert(cls.driver).text

    @classmethod
    def select_dropdown_option_by_value(cls, element_locator, option_value):
        element = cls.find_element(element_locator)
        select = Select(element)
        select.select_by_value(option_value)

    @classmethod
    def select_dropdown_option_by_index(cls, element_locator, index):
        element = cls.find_element(element_locator)
        select = Select(element)
        select.select_by_index(index)

    @classmethod
    def select_dropdown_option_by_visible_text(cls, element_locator, visible_text):
        element = cls.find_element(element_locator)
        select = Select(element)
        select.select_by_visible_text(visible_text)

    @classmethod
    def execute_script(cls, script, *args):
        return cls.driver.execute_script(script, *args)

    @classmethod
    def execute_async_script(cls, script, *args):
        return cls.driver.execute_async_script(script, *args)

    @classmethod
    def get_cookies(cls):
        return cls.driver.get_cookies()

    @classmethod
    def add_cookie(cls, cookie_dict):
        cls.driver.add_cookie(cookie_dict)

    @classmethod
    def delete_cookie(cls, cookie_name):
        cls.driver.delete_cookie(cookie_name)

    @classmethod
    def delete_all_cookies(cls):
        cls.driver.delete_all_cookies()

    @classmethod
    def get_window_size(cls):
        return cls.driver.get_window_size()

    @classmethod
    def get_window_position(cls):
        return cls.driver.get_window_position()

    @classmethod
    def set_browser_size(cls, width, height):
        cls.driver.set_window_size(width, height)

    @classmethod
    def maximize_browser_window(cls):
        cls.driver.maximize_window()

    @classmethod
    def set_browser_position(cls, x, y):
        cls.driver.set_window_position(x, y)

    @classmethod
    def take_element_screenshot(cls, element_locator, filename):
        element = cls.find_element(element_locator)
        element.screenshot(filename)

    @classmethod
    def drag_and_drop(cls, source_element_locator, target_element_locator):
        source_element = cls.find_element(source_element_locator)
        target_element = cls.find_element(target_element_locator)
        ActionChains(cls.driver).drag_and_drop(source_element, target_element).perform()

    @classmethod
    def scroll_to_element(cls, element_locator):
        element = cls.find_element(element_locator)
        cls.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @classmethod
    def scroll_to_bottom(cls):
        cls.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @classmethod
    def switch_to_alert(cls):
        return cls.driver.switch_to.alert

    @classmethod
    def get_all_window_handles(cls):
        return cls.driver.window_handles

    @classmethod
    def wait_for_alert(cls, timeout=10):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return WebDriverWait(cls.driver, timeout).until(
            EC.alert_is_present()
        )

    @classmethod
    def verify_element_present(cls, element_locator):
        try:
            cls.find_element(element_locator)
            cls.logger.info(f"Element located by {element_locator} is present.")
            return True
        except NoSuchElementException as e:
            cls.logger.error(f"Element located by {element_locator} is not present. {e}")
            return False
        except TimeoutException as e:
            cls.logger.error(f"Timeout waiting for element located by {element_locator}. {e}")
            return False
        except Exception as e:
            cls.logger.error(f"An unexpected error occurred: {e}")
            return False

    @classmethod
    def verify_elements_present(cls, elements_locator):
        try:
            cls.is_element_displayed(elements_locator)
            cls.logger.info(f"Element located by {elements_locator} is present.")
            return True
        except NoSuchElementException as e:
            cls.logger.error(f"Element located by {elements_locator} is not present. {e}")
            return False
        except TimeoutException as e:
            cls.logger.error(f"Timeout waiting for element located by {elements_locator}. {e}")
            return False
        except Exception as e:
            cls.logger.error(f"An unexpected error occurred: {e}")
            return False

    @classmethod
    def verify_text_in_element(cls, element_locator, expected_text):
        element = cls.find_element(element_locator)
        actual_text = element.text
        try:
            assert expected_text == actual_text
            cls.logger.info(f"Text in element is as expected: {expected_text}")
            return True
        except AssertionError:
            cls.logger.error(f"Text in element doesn't match. Expected: {expected_text}, Actual: {actual_text}")
            return False

    @classmethod
    def verify_attribute_value(cls, element_locator, attribute, expected_value):
        element = cls.find_element(element_locator)
        actual_value = element.get_attribute(attribute)
        try:
            assert expected_value == actual_value
            cls.logger.info(f"Attribute '{attribute}' has the expected value: {expected_value}")
            return True
        except AssertionError:
            cls.logger.error(
                f"Attribute '{attribute}' value does not match. Expected: {expected_value}, Actual: {actual_value}")
            return False

    @classmethod
    def expect_element_present(cls, element_locator):
        try:
            cls.find_element(element_locator)
            cls.logger.info(f"Element located by {element_locator} is present.")
        except AssertionError:
            cls.logger.error(f"Element located by {element_locator} is not present.")
            raise AssertionError(f"Element located by {element_locator} is not present.")

    @classmethod
    def expect_text_in_element(cls, element_locator, expected_text):
        element = cls.find_element(element_locator)
        actual_text = element.text
        try:
            assert expected_text == actual_text
            cls.logger.info(f"Text in element is as expected: {expected_text}")
        except AssertionError:
            cls.logger.error(f"Text in element doesn't match. Expected: {expected_text}, Actual: {actual_text}")
            raise AssertionError(f"Text in element doesn't match. Expected: {expected_text}, Actual: {actual_text}")

    @classmethod
    def expect_attribute_value(cls, element_locator, attribute, expected_value):
        element = cls.find_element(element_locator)
        actual_value = element.get_attribute(attribute)
        try:
            assert expected_value == actual_value
            cls.logger.info(f"Attribute '{attribute}' has the expected value: {expected_value}")
        except AssertionError:
            cls.logger.error(
                f"Attribute '{attribute}' value does not match. Expected: {expected_value}, Actual: {actual_value}")
            raise AssertionError(
                f"Attribute '{attribute}' value does not match. Expected: {expected_value}, Actual: {actual_value}")

    @classmethod
    def verify_equal(cls, actual, expected, message=None):
        try:
            assert actual == expected, message
            cls.logger.info(f"Verification passed: Actual value '{actual}' is equal to Expected value '{expected}'")
        except AssertionError as e:
            cls.logger.error(f"Verification failed: {str(e)}")
            return False
        return True

    @classmethod
    def verify_not_equal(cls, actual, not_expected, message=None):
        try:
            assert actual != not_expected, message
            cls.logger.info(
                f"Verification passed: Actual value '{actual}' is not equal to Not Expected value '{not_expected}'")
        except AssertionError as e:
            cls.logger.error(f"Verification failed: {str(e)}")
            return False
        return True

    @classmethod
    def expect_equal(cls, actual, expected, message=None):
        try:
            assert actual == expected, message
            cls.logger.info(f"Expectation passed: Actual value '{actual}' is equal to Expected value '{expected}'")
        except AssertionError as e:
            cls.logger.error(f"Expectation failed: {str(e)}")
            raise AssertionError(str(e))

    @classmethod
    def expect_not_equal(cls, actual, not_expected, message=None):
        try:
            assert actual != not_expected, message
            cls.logger.info(
                f"Expectation passed: Actual value '{actual}' is not equal to Not Expected value '{not_expected}'")
        except AssertionError as e:
            cls.logger.error(f"Expectation failed: {str(e)}")
            raise AssertionError(str(e))

    @classmethod
    def exists(cls, func, **args) -> bool:
        loop_wait = 0.05
        timeout = Constants.default_throttle
        params = dict()
        for key, val in args.items():
            if str(key) == "timeout":
                if val is not None:
                    timeout = int(val)
            elif str(key) == 'loop_wait':
                loop_wait = val
            elif str(key) == 'fail_message':
                continue
            else:
                params[key] = val

        first_attempt = True
        found = False
        start_time = time.time()

        while not found and (time.time() - start_time <= timeout or first_attempt):
            # simulate a do-while loop. This is to prevent possible false negatives if the timeout is 0
            first_attempt = False
            if len(params) > 0:
                found = func(**params)
            else:
                found = func()
            if not found:
                time.sleep(loop_wait)

        return found

    # same as exists but throws an actual assert error if not found

    @classmethod
    def verify(cls, func, **args) -> bool:
        if 'fail_message' in args:
            assert_message = args['fail_message']
        else:
            assert_message = 'No assert message given.'

        result = cls.exists(func, **args)

        if hasattr(assert_message, '__call__'):
            assert result is True, assert_message
        else:
            assert result is True, assert_message

        return result

    @classmethod
    def verify_comparison(cls, expected, actual, fail_message=None):
        """
        Uses verify to perform a straight comparison. Actual can take a function signature or string value.
        This function will also format the fail message.
        :param expected: A string, int, float, boolean, or iterable to serve as the expected value.
        :param actual: If this is an instance method, pass this in as a signature (ie, no parenthesis).
        :param fail_message: Message to send to console on failure
        :return:
        """
        if inspect.ismethod(actual):
            cls.verify(lambda: actual() == expected,
                       fail_message=cls.get_formatted_fail_message(expected, actual(), fail_message))
        else:
            cls.verify(lambda: actual == expected,
                       fail_message=cls.get_formatted_fail_message(expected, actual, fail_message))

    @classmethod
    def get_formatted_fail_message(cls, expected, actual, error_message=None):
        if error_message is None:
            error_message = 'The actual value does not match the expected value.'
        return "{0}\nExpected: '{1}'\nActual: '{2}'".format(error_message, expected, actual)

    @classmethod
    def assert_equals_with_message(cls, expected_value, actual_value,
                                   error_message="The actual value does not match the expected value."):
        """
        Asserts if two values are equal. If they are not, outputs a message displaying both values.
        :param expected_value: Expected value
        :param actual_value: Actual value
        :param error_message: Message to send to console on failure
        """

        assert actual_value == expected_value, (
            cls.get_formatted_fail_message(expected_value, actual_value, error_message))

    @classmethod
    def verify_horizontal_vertical_order(cls, element_array):
        """
        Verify the horizontal and vertical order of a "grid" array passed in
        :param element_array: Accepts a two-dimensional array with the horizontal/vertical position of elements to
                              verify Each row in the array corresponds to a SPECIFIC Y position, so any offset elements
                              will need their own row
        :return: None
        """

        # loop through each row. First verify the horizontal order of that row
        prev_row_y = -1
        for row_index, row in enumerate(element_array):
            cur_row_y = None
            prev_col_x = -1
            for col_index, col in enumerate(row):
                # verify all elements in the row have the same Y position
                if cur_row_y is not None:
                    assert math.floor(col.get_element_location()['y']) == cur_row_y, \
                        "Row {0}, Col {1} not at same Y height".format(row_index, col_index)

                cur_row_y = math.floor(col.get_element_location()['y'])
                # verify the row's Y position is in the correct order
                assert math.floor(col.get_element_location()['y']) > prev_row_y

                # verify all columns in the row are in the correct order
                assert math.floor(col.get_element_location()['x']) > prev_col_x, \
                    "Row {0}, Col {1} incorrect X position".format(row_index, col_index)
                prev_col_x = math.floor(col.get_element_location()['x'])

            prev_row_y = cur_row_y

    # delayed assert/soft failure

    @classmethod
    def expect(cls, expr, **args):
        if 'fail_message' in args:
            expect_message = "Failure: {0}".format(args['fail_message'])
        else:
            expect_message = "Failure: No expect message given"

        if 'take_screenshot' in args:
            bool_take_screenshot = args['take_screenshot']
        else:
            bool_take_screenshot = True

        if "timeout" in args:
            timeout = args['timeout']
        else:
            timeout = None

        result = cls.exists(expr, timeout=timeout)

        if result is not True:
            cls.logger.info(logging.INFO, msg=expect_message, log_take_screenshot=bool_take_screenshot)
        return result

    @classmethod
    def expect_comparison(cls, expected, actual, fail_message=None, screenshot=True, timeout=None):
        """
        Uses expect to perform a straight comparison. Actual can take a function signature or string value.
        This function will also format the fail message.
        :param timeout:
        :param expected: A string, int, float, boolean, or iterable to serve as the expected value.
        :param actual: If this is an instance method, pass this in as a signature (ie, no parenthesis).
        :param fail_message: str
        :param screenshot: bool
        :return:
        """

        def actual_value():
            return actual() if inspect.ismethod(actual) else actual

        cls.expect(lambda: actual_value() == expected,
                   fail_message=cls.get_formatted_fail_message(expected, actual_value(), fail_message),
                   take_screenshot=screenshot, timeout=timeout)

    @classmethod
    def get_clipboard_data(cls):
        win32clipboard.OpenClipboard()
        clipboard_data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
        win32clipboard.CloseClipboard()
        return clipboard_data.decode('utf-8')

    @classmethod
    def set_clipboard_data(cls, data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_TEXT, data.encode('utf-8'))
        win32clipboard.CloseClipboard()

    @classmethod
    def empty_lines_formatter(cls, string):
        # When we get notes from new editor, every empty line returns extra \n (2 instead of 1).
        # We use this function to format notes returned from React notes editor.
        formatted_string = ''
        n_count = 0

        for i, s in enumerate(string):
            next_el_ind = i + 1
            if s == '\n':
                n_count += 1
                if (next_el_ind < len(string)) and (string[next_el_ind] == '\n'):
                    pass
                else:
                    # remove extra /n
                    extra_chars = n_count // 2
                    formatted_string += '\n' * (n_count - extra_chars)
                    n_count = 0
            else:
                formatted_string += s

        return formatted_string

    @classmethod
    def get_screenshot_as_file(cls, filename):
        cls.driver.get_screenshot_as_file(filename)

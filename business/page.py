import json
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By


class Page(object):
    def __init__(self, browser, page_name='Home'):
        self._browser = browser
        self.page_name = page_name
        self._elements_definitions = None
        self._load_elements_def()

    @property
    def browser(self):
        return self._browser

    def _get_element(self, element_name, timeout=5):
        element_def = self._get_element_def(element_name)
        return self._browser.get_element(element_def, timeout)

    def _load_elements_def(self):
        elements_json_folder = self._browser.json_data["defs_folder"]
        path = os.path.join(elements_json_folder, self.page_name + '.json')
        if os.path.exists(path):
            with open(path) as file:
                self._elements_definitions = json.loads(file.read())
        else:
            raise Exception('Elements definition file for page {} not found'.format(self.page_name))

    def _get_element_def(self, element_name):
        element_def = self._elements_definitions.get(element_name, None)
        if not element_def:
            raise Exception('Element definition not found')
        return element_def

    def write(self, element_name, text):
        el = self._get_element(element_name)
        el.clear()
        el.send_keys(text)

    def wait(self, seconds):
        time.sleep(seconds)

    def click(self, element_name):
        el = self._get_element(element_name)
        try:
            el.click()
        except ElementNotInteractableException:
            self._browser._driver.execute_script('arguments[0].click()', el)

    def _wait_for_element(self, element_name, timeout=5):
        el = self._get_element(element_name, timeout)
        if not el:
            raise Exception("Element not found: {element}".format(element=element_name))
        return el

    def wait_element_is_visible(self, element_name, xpath=None, timeout=30):
        if xpath:
            wait = WebDriverWait(self._browser._driver, timeout)
            wait.until(EC.visibility_of_element_located(By.XPATH(xpath)))
        else:
            self._wait_for_element(element_name, timeout)

    def wait_element_is_clickable(self, element_name, xpath=None, timeout=5):
        def get_el(self, el_name, seconds):
            elm = self._wait_for_element(el_name, seconds)
            return elm.is_enabled()

        is_clickable = False
        if element_name:
            for _ in range(timeout):
                is_clickable = get_el(self, element_name, timeout)
                if is_clickable:
                    break
                time.sleep(1)
            if not is_clickable:
                raise Exception('Element not clickable')
        elif xpath:
            wait = WebDriverWait(self._browser._driver, timeout)
            wait.until(EC.element_to_be_clickable(By.XPATH(xpath)))

    def press_key(self, element_name, key):
        el = self._get_element(element_name)
        special_key = getattr(Keys, key.upper(), None)
        el.send_keys(special_key)

    def read(self, element_name=None, xpath=None):
        el = None
        if element_name:
            el = self._get_element(element_name)
        elif xpath:
            for _ in range(15):
                try:
                    el = self._browser._driver.find_element_by_xpath(xpath)
                    if el:
                        break
                except:
                    time.sleep(1)
                    continue
        if el:
            return el.text
        else:
            raise Exception('Element not found')

















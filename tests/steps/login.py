import json, time
from base.browser import Browser
from business.page import Page

def open_site():
    file_path = '..\\test_data\\environment.json'
    with open(file_path) as file:
        data = json.loads(file.read())
        if data:
            browser = Browser()
            browser.start()
            browser.get(data['url'])
            browser.maximize_window()
            login_page = Page(browser, 'Login')
        else:
            raise AssertionError('No data available for site')
        return browser, login_page


def login(page, user, password):
    page.write('Username', user)
    page.click('Continue')
    page.wait_element_is_visible('Login')
    time.sleep(5)
    page.click('Password')
    page.write('Password', password)
    page.click('Login')
    xpath = '//p[contains(@class,\"MuiTypography-root avatar\")]'
    for _ in range(30):
        try:
            avatar = page._browser._driver.find_element_by_xpath(xpath)
            if avatar:
                break
        except:
            time.sleep(1)
            continue
    return Page(page.browser, 'MainPage')


def logout(page):
    page.click('Avatar')
    page.wait_element_is_visible('Logout')
    page.click('Logout')



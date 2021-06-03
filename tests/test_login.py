import pytest
from tests.steps.login import *


@pytest.fixture()
def initial_page():
    browser, login_page = open_site()
    yield login_page
    browser.stop()


def test_login(initial_page):
    user = "ci_cd+qa_challenge01@attackiq.com"
    password = "testChallenge01"
    new_password = "HappyTesting1"

    login_page = initial_page
    login_page.wait_element_is_visible('Username')
    main_page = login(login_page, user, password)
    main_page.click('Avatar')
    main_page.wait_element_is_visible('Logout')
    main_page.click('Change Password')
    main_page.wait_element_is_visible('Current Password')
    main_page.write('Current Password', password)
    main_page.write('New Password', new_password)
    main_page.write('Confirm Password', new_password)
    main_page.click('Save')
    time.sleep(3)
    xpath = "//table[@data-testid='success-toast-content']"
    toast_success = main_page.browser._driver.find_element_by_xpath(xpath)
    assert toast_success is not None, 'Password change failed'

    # logged_user_xpath = "//span[text()='ci_cd+qa_challenge01@attackiq.com']"
    # logged_user_value = main_page.read(xpath=logged_user_xpath)
    # assert logged_user_value == user, 'Current user does not match values entered upon login'











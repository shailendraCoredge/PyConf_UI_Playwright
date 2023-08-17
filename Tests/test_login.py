import time
import pytest

from Pages.login_page import LoginPage
from Resources.users_data import users

@pytest.mark.parametrize("username, password", users)
def test_login_with_valid_user(page, username, password):
    login_page = LoginPage(page)
    login_page.navigateTo()
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login()

    assert page.url == 'https://www.saucedemo.com/v1/inventory.html'

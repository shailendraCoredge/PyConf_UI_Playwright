import time
import pytest

from Pages.login_page import LoginPage
from Pages.product_page import ProductPage



def test_Item_add_to_cart(page):
    login_page = LoginPage(page)
    login_page.login_app("standard_user", "secret_sauce")
    product_page = ProductPage(page)
    product_page.click_add_item_in_cart()
    assert product_page.get_cart_item_count() == '1'





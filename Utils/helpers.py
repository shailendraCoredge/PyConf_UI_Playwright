import time

import pytest


def locate_all_xpath(page, xpath):
    try:
        elements = page.locator(xpath).all()
        return elements
    except Exception as e:
        print(f"Locator {xpath} is not available on the page: {e}")
        return []



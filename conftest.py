import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption('--browserr', action='store', default='chrome')
    parser.addoption('--headless', action='store', type=bool, default=False)


@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope='session')
def browser(request):
    print('browser is generating again and again ________________________________________')
    global browser

    browser_name = request.config.getoption('--browserr')

    play = sync_playwright().start()

    if browser_name == 'chrome':
        browser = play.chromium.launch(headless=request.config.getoption('--headless'))

    elif browser_name == 'firefox':
        browser = play.firefox.launch(headless=request.config.getoption('--headless'))

    elif browser_name == 'webkit':
        browser = play.webkit.launch(headless=request.config.getoption('--headless'))

    else:
        print(f"{browser_name} browser is not available!")

    yield browser

    browser.close()
    play.stop()

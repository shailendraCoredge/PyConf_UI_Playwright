class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("//input[@id='user-name']")
        self.password_input = page.locator("//input[@id='password']")
        self.login_button = page.locator("//input[@id='login-button']")

    def navigateTo(self):
        self.page.goto('https://www.saucedemo.com/v1/')

    def input_username(self, username):
        self.username_input.fill(username)

    def input_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login_app(self, username, password):
        self.navigateTo()
        self.input_username(username)
        self.input_password(password)
        self.click_login()
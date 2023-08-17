class ProductPage:
    def __init__(self, page):
        self.page = page
        self.add_cart_item = page.locator("//*[@id='inventory_container']/div/div[1]/div[3]/button")
        self.cart_item = page.locator("//span[@class='fa-layers-counter shopping_cart_badge']")


    def click_add_item_in_cart(self):
        self.add_cart_item.click()

    def get_cart_item_count(self):
        return self.cart_item.inner_text()

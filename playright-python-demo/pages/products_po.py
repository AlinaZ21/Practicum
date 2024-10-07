class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_backpack_button = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.add_to_cart_bike_button = page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        self.cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
        self.count_in_cart = page.locator("[data-test=\"shopping-cart-badge\"]")
        self.remove_bike_from_cart_button = page.locator("[data-test=\"remove-sauce-labs-bike-light\"]")

    def add_to_cart_two_products(self) -> None:
        self.add_to_cart_backpack_button.click()
        self.add_to_cart_bike_button.click()

    def remove_one_from_cart(self) -> None:
        self.remove_bike_from_cart_button.click()

    def go_to_cart(self) -> None:
        self.cart_link.click()

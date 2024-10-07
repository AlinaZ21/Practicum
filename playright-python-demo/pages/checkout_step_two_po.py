class CheckoutStepTwoPage:
    def __init__(self, page):
        self.page = page
        self.finish_button = page.locator("[data-test=\"finish\"]")
        self.message = page.locator("[data-test=\"complete-header\"]")
    
    def finish_order(self) -> None:
        self.finish_button.click()
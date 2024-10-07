class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page
        self.header = page.locator("[data-test=\"complete-header\"]")

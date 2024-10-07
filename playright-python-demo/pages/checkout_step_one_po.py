class CheckoutStepOnePage:
    def __init__(self, page):
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.name = page.locator("[data-test=\"firstName\"]")
        self.surname = page.locator("[data-test=\"lastName\"]")
        self.code = page.locator("[data-test=\"postalCode\"]")

    def enter_data(self, name: str, surname: str, code: str) -> None:
        self.name.fill(name)
        self.surname.fill(surname)
        self.code.fill(code)
        self.continue_button.click()

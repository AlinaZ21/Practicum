from playwright.sync_api import expect
from pages.login_po import LoginPage
from pages.products_po import ProductsPage
from pages.cart_po import CartPage  
from pages.checkout_step_one_po import CheckoutStepOnePage
from pages.checkout_step_two_po import CheckoutStepTwoPage
from pages.checkout_complete_po import CheckoutCompletePage

def test_empty_login(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_step_one_page = CheckoutStepOnePage(page)
    checkout_step_two_page = CheckoutStepTwoPage(page)
    complete_page = CheckoutCompletePage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_to_cart_two_products()
    products_page.go_to_cart()

    cart_page.checkout_to_order()

    checkout_step_one_page.enter_data("name", "surname", "code@yandex.ru")

    checkout_step_two_page.finish_order()

    expect(complete_page.header).to_contain_text("Thank you for your order!")

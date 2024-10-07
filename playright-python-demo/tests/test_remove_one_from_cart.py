from playwright.sync_api import expect
from pages.login_po import LoginPage
from pages.products_po import ProductsPage

def test_add_one_to_cart(page):
    login_page = LoginPage(page)
    productsPage = ProductsPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    productsPage.add_to_cart_two_products()
    expect(productsPage.count_in_cart).to_be_visible()
    expect(productsPage.count_in_cart).to_contain_text("2")
    productsPage.remove_one_from_cart()
    expect(productsPage.count_in_cart).to_contain_text("1")

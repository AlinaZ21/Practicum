from playwright.sync_api import expect
from pages.login_po import LoginPage

def test_incorrect_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("unknown_user", "secret_sauce")
    expect(login_page.error).to_contain_text("Epic sadface: Username and password do not match any user in this service")

from .pages.product_page import ProductPage
import pytest

links = ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"]

@pytest.mark.parametrize("books", links)
def test_guest_can_add_product_to_basket(browser, books):
    link = books
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button()
    page.solve_quiz_and_get_code()
    page.add_product_to_basket()

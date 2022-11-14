from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_to_basket_button(browser):
    browser.get(link)
    button_add_to_basket = None
    try:
        button_add_to_basket = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    except:
        pass

    assert button_add_to_basket == None, "Add to basket button not found"
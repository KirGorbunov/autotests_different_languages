from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_to_basket_button(browser):
    browser.get(link)
    button_add_to_basket = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    print(button_add_to_basket.get_attribute('disabled'))
    assert button_add_to_basket.get_attribute('disabled') == None, "Add to cart button "
import time


def test_items(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(3)
    assert browser.find_elements_by_css_selector('.btn-add-to-basket'), \
        'Element is not found on the page'

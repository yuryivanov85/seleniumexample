import pytest


@pytest.mark.parametrize("item", [
    "macbook pro",
    "mac mini",
    "gaming laptop"
])
@pytest.mark.regressiontest
def test_amazon_search_title_multiple(browser, item):
    browser.get("https://www.amazon.com")
    browser.find_element_by_id("twotabsearchtextbox").send_keys(item)
    browser.find_element_by_id("nav-search-submit-button").click()
    assert browser.title == "Amazon.com : " + item


import pytest


@pytest.mark.smoketest
def test_amazon_navigation(browser):
    browser.get("https://www.amazon.com")
    assert browser.title == "Amazon.com. Spend less. Smile more."



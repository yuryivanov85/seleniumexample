import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()
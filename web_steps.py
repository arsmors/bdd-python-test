import pytest
from pytest_bdd import scenario, parsers, given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@scenario('web.feature', 'Basic DuckDuckGo search')
def test_arguments():
    pass

@pytest.fixture
def browser():
    b = webdriver.Chrome('./chromedriver.exe')
    #b.implicity_wait(10)
    yield b
    b.quit()


@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    browser.get('https://duckduckgo.com/')


@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(phrase + Keys.RETURN)


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    xpath = "//div[@id='links']//*[contains(text(), '%s')]" % phrase
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0

    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase

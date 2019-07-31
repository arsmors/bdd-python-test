from pytest_bdd import scenarios, parsers, given, when, then, scenario

from cucumbers import CucumberBasket
import pytest

CONVENTERS = dict(initial=int, some=int, total=int)
scenarios('cucumber_scenario.feature', example_converters=CONVENTERS)

@given('the basket has "<initial>" cucumbers')
@given(parsers.cfparse('the basket has "{initial:d}" cucumbers'))
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when('"<some>" cucumbers are added to the basket')
@when(parsers.cfparse('"{some:d}" cucumbers are added to the basket'))
def add_cucumbers(basket, some):
    basket.add(some)

@then('the basket contains "<total>" cucumbers')
@then(parsers.cfparse('the basket contains "{total:d}" cucumbers'))
def basket_has_total(basket, total):
    assert basket.count == total

from pytest_bdd import scenario, parsers, given, when, then

from cucumbers import CucumberBasket
import pytest


@scenario('cucumber.feature', 'Add cucumbers to a basket')
def test_arguments():
    pass


@given(parsers.cfparse('the basket has "{initial:d}" cucumbers', extra_types=dict(d=int)))
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('"{some:d}" cucumbers are added to the basket', extra_types=dict(d=int)))
def add_cucumbers(basket, some):
    basket.add(some)


@then(parsers.cfparse('the basket contains "{total:d}" cucumbers', extra_types=dict(d=int)))
def basket_has_total(basket, total):
    assert basket.count == total

import re
from pytest_bdd import scenario, given, when, then, parsers
from pytest_bdd.parsers import re
import pytest


@scenario('test.feature', 'Arguments for given, when, thens')
def test_arguments():
    pass

@scenario('test.feature', 'Arguments for given, when, thens negative')
def test_arguments():
    pass

@given(re('there are (?P<number>.*) cucumbers'))
def start_cucumbers(context, number):
    print("there are 5 cucumbers")
    context.total = number
    # return dict(start = start, eat =0)


@when(re('I eat (?P<number>.*) cucumbers'))
def eat_cucumbers(context, number):
    print("I eat 3 cucumbers")
    context.eat = number
    # start_cucumbers['eat'] +=eat


@then(re('I should have (?P<number>.*) cucumber'))
def should_have_left_cucumbers(context, number):
    assert int(number) == (int(context.total) - int(context.eat))
    print("I should have 2 cucumber", number)
    # assert start_cucumbers['start'] == start
    # assert start - start_cucumbers['eat'] == left


class Context:
    pass


@pytest.fixture
def context():
    return Context()

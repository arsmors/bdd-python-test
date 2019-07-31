Feature: Cucumber Basket

  Scenario Outline: Add cucumbers to a basket scenario
    Given the basket has "<initial>" cucumbers
    When "<some>" cucumbers are added to the basket
    Then the basket contains "<total>" cucumbers

    Examples: Cucumber Counts
      | initial | some | total |
      | 0       | 3    | 3     |
      | 2       | 4    | 6     |
      | 5       | 5    | 10    |

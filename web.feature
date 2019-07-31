Feature: DuckDuckGo web Browsing
  As a web surfer,
  I want ot find info online




  Scenario: Basic DuckDuckGo search
    Given the DuckDuckGo home page is displayed
    When the user searches for "panda"
    Then results are shown for "panda"

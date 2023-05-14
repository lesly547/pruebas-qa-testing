Feature: Search WEB duckduckgo
  Scenario: User searches in web duckduckgo
    Given open duckduckgo web
    When user searches Toledo on the web
    Then enter to Toledo - Wikipedia result
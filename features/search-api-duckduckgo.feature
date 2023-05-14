Feature: Search API duckduckgo
  Scenario: User searches API duckduckgo
    Given API duckduckgo
    When user search Toledo
    Then response code is 200
    And the source result AbstractSource is Wikipedia
    And create list with fields AbstractURL and FirstURL in RelatedTopics
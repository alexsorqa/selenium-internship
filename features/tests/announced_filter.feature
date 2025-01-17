Feature: Filter scenarios

  Scenario: User can filter by Announced
    Given Open Main Page
    Then Log in to the page with alexsorqa@gmail.com and alexsorqa
    When Click on Off-Plan at side menu
    Then Select Announced in Sales status menu
    And Verify each product contains Announced
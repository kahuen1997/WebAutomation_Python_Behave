Feature: Maven Repository

  Background:
    Given U open the broswer
    When U open the website

  Scenario Outline:
    When U enter the name of search "<searchbar>"
    Then U click Search Button
    And User Verfiy page and close the browser

    Examples:
      | searchbar |
      | Selenium |
      | Junit    |
      | Testng   |

    Scenario:
      When U click the chart
      And User Verfiy page and close the browser

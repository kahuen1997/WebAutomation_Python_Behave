Feature: Facebook Register New Account Setting
#  https://www.facebook.com/r.php?locale=zh_TW&display=page

  Scenario Outline: Enter the form of data
    Given User Launch the Browser
    When User Go to Facebook Page
    And User Fill in the name"<Name>"
    And User fill in the birth"<Birth>"
    Then User Click Submit
    And quit browser

    Examples:
      | Name | Birth |
      | Mike | 2000  |
      | Jack | 1997  |


Feature: search settings title

  @searchTitle
  Scenario Outline: Testing search title in settings
    Given open menu
    When select settings
    Then verify title "<title>" and close

    Examples:
      | title         |
      | Apps          |
      | Notifications |
      | Fer           |

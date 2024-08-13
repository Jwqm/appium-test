Feature: Login functionality in the Tunki app

  Scenario: Successful login attempt with valid credentials
    Given the Tunki app is opened
    When I allow the notification permission if prompted
    And I click on the "Login" button
    And I enter my mobile number as "030345612"
    And I accept the entered mobile number
    And I enter my password using the on-screen keypad
    And I click on the "Login" button
    Then I should see an error message displayed
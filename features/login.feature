Feature: Sauce Application Login Feature
  Scenario: Invalid user

    Given i open the browser
    When i enter the application url
    And i enter invalid user
    And i enter invalid password
    And i click login button
    Then i verify the invalid user message


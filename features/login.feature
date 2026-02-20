Feature: User Login
  As a user
  I want to log into the application
  So that I can access my account

  Background:
    Given I am on the login page

  @smoke @login
  Scenario: Successful login with valid credentials
    When I enter username "testuser@example.com"
    And I enter password "Test@123"
    And I click the login button
    Then I should see the dashboard

  @negative @login
  Scenario: Failed login with invalid credentials
    When I enter username "invalid@example.com"
    And I enter password "wrongpassword"
    And I click the login button
    Then I should see error message "Invalid credentials"

  @login
  Scenario Outline: Login with different users
    When I login with username "<username>" and password "<password>"
    Then I should see "<result>"

    Examples:
      | username              | password    | result     |
      | admin@example.com     | Admin@123   | Dashboard  |
      | user@example.com      | User@123    | Dashboard  |

@todomvc
Feature: TodoMVC Application Testing
  As a user
  I want to manage my todo list
  So that I can track my tasks

  Background:
    Given I am on the TodoMVC page

  @smoke
  Scenario: Add a new todo item
    When I add a new todo "Buy groceries"
    Then I should see "Buy groceries" in the todo list
    And the todo count should be 1

  @smoke
  Scenario: Mark todo as complete
    Given I have added a todo "Complete homework"
    When I mark the todo as complete
    Then the todo should be marked as completed
    And the active count should be 0

  Scenario: Delete a todo item
    Given I have added a todo "Old task"
    When I delete the todo
    Then I should not see "Old task" in the todo list
    And the todo count should be 0

  Scenario: Add multiple todos
    When I add a new todo "Task 1"
    And I add a new todo "Task 2"
    And I add a new todo "Task 3"
    Then the todo count should be 3

  Scenario: Filter active todos
    Given I have added a todo "Active task"
    And I have added a todo "Completed task"
    And I have marked "Completed task" as complete
    When I click on "Active" filter
    Then I should see "Active task" in the todo list
    And I should not see "Completed task" in the todo list

  Scenario: Filter completed todos
    Given I have added a todo "Active task"
    And I have added a todo "Completed task"
    And I have marked "Completed task" as complete
    When I click on "Completed" filter
    Then I should see "Completed task" in the todo list
    And I should not see "Active task" in the todo list

  Scenario: Clear completed todos
    Given I have added a todo "Task 1"
    And I have added a todo "Task 2"
    And I have marked "Task 1" as complete
    When I click "Clear completed"
    Then I should not see "Task 1" in the todo list
    And I should see "Task 2" in the todo list

Feature: To-Do List Management
  In order to manage tasks effectively,
  As a user,
  I want to add, list, modify, and manage the status of tasks in my to-do list.

  Scenario: Adding a task
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries" with status "Pending"

  Scenario: Listing all tasks
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
      | Pay bills     | Pending |
    When the user lists all tasks
    Then the output should contain:
      | Task          | Status  |
      | Buy groceries | Pending |
      | Pay bills     | Pending |

  Scenario: Marking a task as completed
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" with status "Completed"

  Scenario: Clearing the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Attempting to add an empty task
    Given the to-do list is empty
    When the user adds a task ""
    Then an error message "Task description cannot be empty" should be displayed

  Scenario: Trying to mark a non-existent task as completed
    Given the to-do list contains tasks:
      | Task      | Status  |
      | Pay bills | Pending |
    When the user marks task "Buy groceries" as completed
    Then an error message "Task 'Buy groceries' not found" should be displayed

  Scenario: Attempting to mark an already completed task as completed
    Given the to-do list contains tasks:
      | Task          | Status    |
      | Buy groceries | Completed |
    When the user marks task "Buy groceries" as completed
    Then a message "Task 'Buy groceries' is already completed" should be displayed

  Scenario: Adding a duplicate task
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user adds a task "Buy groceries"
    Then an error message "Task 'Buy groceries' already exists" should be displayed
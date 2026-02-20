"""
TodoMVC Step Definitions
For testing https://demo.playwright.dev/todomvc/
"""
from behave import given, when, then
from playwright.sync_api import expect

@given('I am on the TodoMVC page')
def step_navigate_to_todomvc(context):
    """Navigate to TodoMVC application"""
    context.page.goto("https://demo.playwright.dev/todomvc/")
    print("✓ Navigated to TodoMVC")

@given('I have added a todo "{todo_text}"')
def step_add_todo_given(context, todo_text):
    """Add a todo as precondition"""
    input_box = context.page.locator(".new-todo")
    input_box.fill(todo_text)
    input_box.press("Enter")
    print(f"✓ Added todo (setup): {todo_text}")

@given('I have marked "{todo_text}" as complete')
def step_mark_complete_given(context, todo_text):
    """Mark a specific todo as complete"""
    # Find the todo by text and click its checkbox
    todo_item = context.page.locator(f"li:has-text('{todo_text}')")
    checkbox = todo_item.locator(".toggle")
    checkbox.click()
    print(f"✓ Marked as complete: {todo_text}")

@when('I add a new todo "{todo_text}"')
def step_add_new_todo(context, todo_text):
    """Add a new todo item"""
    input_box = context.page.locator(".new-todo")
    input_box.fill(todo_text)
    input_box.press("Enter")
    print(f"✓ Added new todo: {todo_text}")

@when('I mark the todo as complete')
def step_mark_todo_complete(context):
    """Mark the first todo item as complete"""
    checkbox = context.page.locator(".todo-list li").first.locator(".toggle")
    checkbox.click()
    print("✓ Marked todo as complete")

@when('I delete the todo')
def step_delete_todo(context):
    """Delete the first todo item"""
    todo_item = context.page.locator(".todo-list li").first
    todo_item.hover()
    delete_button = todo_item.locator(".destroy")
    delete_button.click()
    print("✓ Deleted todo")

@when('I click on "{filter_name}" filter')
def step_click_filter(context, filter_name):
    """Click on a filter (All, Active, Completed)"""
    context.page.click(f"text={filter_name}")
    print(f"✓ Clicked {filter_name} filter")

@when('I click "{button_text}"')
def step_click_button(context, button_text):
    """Click a button by text"""
    context.page.click(f"text={button_text}")
    print(f"✓ Clicked: {button_text}")

@then('I should see "{text}" in the todo list')
def step_verify_todo_in_list(context, text):
    """Verify todo text appears in the list"""
    todos = context.page.locator(".todo-list li")
    expect(todos).to_contain_text(text)
    print(f"✓ Found in list: {text}")

@then('I should not see "{text}" in the todo list')
def step_verify_todo_not_in_list(context, text):
    """Verify todo text does NOT appear in the list"""
    todos = context.page.locator(".todo-list li")
    count = todos.count()
    
    if count == 0:
        print("✓ Todo list is empty")
        return
    
    # Check that none of the todos contain the text
    for i in range(count):
        todo_text = todos.nth(i).text_content()
        assert text not in todo_text, f"Found '{text}' but it should not be visible"
    
    print(f"✓ Verified '{text}' is not in list")

@then('the todo count should be {count:d}')
def step_verify_todo_count(context, count):
    """Verify the number of todos"""
    todos = context.page.locator(".todo-list li")
    actual_count = todos.count()
    assert actual_count == count, f"Expected {count} todos, but found {actual_count}"
    print(f"✓ Todo count is correct: {count}")

@then('the todo should be marked as completed')
def step_verify_todo_completed(context):
    """Verify first todo has completed class"""
    first_todo = context.page.locator(".todo-list li").first
    expect(first_todo).to_have_class("completed")
    print("✓ Todo is marked as completed")

@then('the active count should be {count:d}')
def step_verify_active_count(context, count):
    """Verify the active todo count"""
    count_element = context.page.locator(".todo-count strong")
    actual_count = int(count_element.text_content())
    assert actual_count == count, f"Expected {count} active todos, but found {actual_count}"
    print(f"✓ Active count is correct: {count}")

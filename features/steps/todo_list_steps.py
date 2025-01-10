to_do_list = [] 

@given('the to-do list is empty')
def step_impl(context):
    global to_do_list
    to_do_list = []  

@given('the to-do list contains tasks')
def step_impl(context):
    global to_do_list
    to_do_list = []
    for row in context.table:
        to_do_list.append({"Task": row["Task"], "Status": row["Status"] if "Status" in row else "Pending"})

@when('the user adds a task "{task}"')
def step_impl(context, task):
    global to_do_list
    if not task.strip():
        context.error = "Task description cannot be empty"
    elif any(t["Task"] == task for t in to_do_list):
        context.error = f"Task '{task}' already exists"
    else:
        to_do_list.append({"Task": task, "Status": "Pending"})

@when('the user lists all tasks')
def step_impl(context):
    context.listed_tasks = [{"Task": t["Task"], "Status": t["Status"]} for t in to_do_list]

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    task_found = False
    for t in to_do_list:
        if t["Task"] == task:
            if t["Status"] == "Completed":
                context.error = f"Task '{task}' is already completed"
            else:
                t["Status"] = "Completed"
            task_found = True
            break
    if not task_found:
        context.error = f"Task '{task}' not found"

@when('the user clears the to-do list')
def step_impl(context):
    global to_do_list
    to_do_list = []

@then('the to-do list should contain "{task}" with status "{status}"')
def step_impl(context, task, status):
    task_found = any(t["Task"] == task and t["Status"] == status for t in to_do_list)
    assert task_found, f'Task "{task}" with status "{status}" not found in the to-do list. List: {to_do_list}'

@then('the output should contain:')
def step_impl(context):
    expected_tasks = [{"Task": row['Task'], "Status": row['Status']} for row in context.table]
    assert context.listed_tasks == expected_tasks, f'Expected {expected_tasks}, but got {context.listed_tasks}'

@then('the to-do list should be empty')
def step_impl(context):
    assert len(to_do_list) == 0, f'To-do list is not empty: {to_do_list}'

@then('an error message "{error_msg}" should be displayed')
def step_impl(context, error_msg):
    assert hasattr(context, 'error'), "Error message not found"
    assert context.error == error_msg, f"Unexpected error: {context.error}. Context: {context.__dict__}"  
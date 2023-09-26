from lib.todo_list_td import TodoList
from lib.todo_td import Todo

"""
adds three tasks to the list of todos and return 2 tasks still incomplete

"""

def test_add_three_tasks_return_list_of_incomplete_todos():
    todo_list = TodoList()
    todo_1 = Todo("Task 1")
    todo_2 = Todo("Task 2")
    todo_3 = Todo("Task 3")
    todo_3.mark_complete()
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    assert todo_list.incomplete() == [todo_1, todo_2]


"""
mark complete for all the tasks

"""

def test_give_up_success():
    todo_list = TodoList()
    todo_1 = Todo("Task 1")
    todo_2 = Todo("Task 2")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.give_up()
    assert todo_list.complete() == [todo_1, todo_2]
#!/usr/bin/python3
"""Write a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user_todo = url + "/user/{}/todos".format(argv[1])
    username_id = url + "/users/{}".format(argv[1])
    todo_result = get(user_todo).json()
    name_result = get(username_id).json()

    todo_num = len(todo_result)
    todo_complete = len([todo for todo in todo_result
                         if todo.get("completed")])
    name = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_num))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))

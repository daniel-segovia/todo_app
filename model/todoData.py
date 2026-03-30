def print_list():
    with open("model/todo.csv", "r") as todoList:
        print(todoList.read())

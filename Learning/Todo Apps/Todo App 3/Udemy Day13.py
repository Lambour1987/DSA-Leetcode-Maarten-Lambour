def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return filepath


def write_todos(todos_arg, filepath ="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        #todos = get_todos(filepath="todos.txt")
        todos = get_todos()

        todos.append(todo + '\n')

        #write_todos(filepath="todos.txt", todos_arg=todos)
        #write_todos(filepath = "todos.txt", todos_arg=todos)
        write_todos(todos, "todos.txt")

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item, in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos("todos.txt,",todos)
        except ValueError:
            print("Your comment is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            #todos = get_todos("todos.txt")
            write_todos("todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
        continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print('Bye!')
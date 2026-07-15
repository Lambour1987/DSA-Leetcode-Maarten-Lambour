#Function arguments: Zelf: Custom Function with 1 argument. Default arguments
def get_todos(filepath="todos.txt"):
    with open(filepath,'r') as file:
        todos_local = file.readlines()
    return todos_local

#Multiple Arguments: Zelf: Custom Function with multiple arguments. Default arguments
#todos_arg: non default parametr. filepath="todos.txt" = default parameter

def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos(filepath="todos.txt")

        todos.append(todo + '\n')

        write_todos(todos_arg=todos, filepath="todos.txt")

    elif user_action.startswith('show'):

        todos = get_todos(filepath="todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos(filepath="todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos_arg=todos, filepath="todos.txt")

        except ValueError:
            print("Your comment is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos(filepath="todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos_arg=todos, filepath="todos.txt")

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
        continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

Print('Bye')

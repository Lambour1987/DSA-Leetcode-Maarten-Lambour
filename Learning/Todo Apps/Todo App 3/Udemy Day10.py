while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

#Dus elif ipv if gebruiken. Dan voert hij niet de volledige code uit.

    # match user_action:
    #     case 'add':

    #if 'add' in user_action:
    if user_action.startswith("add"):
        #todo = input("Enter a todo: ") + "\n"
        todo = user_action[4:]

        # Oude manier. Maar zo werkt het intern
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        # Oude manier:
        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    # case 'show':
    #if 'show' in user_action:
    #elif 'show' in user_action:
    elif user_action.startswith("show"):
        # Oude manier
        #file = open('todos.txt', 'r')
        #todos.file.readlines()
        #file.close()

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item, in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    #case 'edit':
    #if 'edit' in user_action:
    #elif 'edit' in user_action:
    elif user_action.startswith("edit"):
        try:
            # number = int(input("Number of the todo to edit: "))
            number = int(user_action[5:])
            print(number)

            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            print('Here is todos existing', todos)


            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            #print('Here is how it will be', todos)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your comment is not valid.")
            #user_action = input("Type add, show, edit, complete or exit: ")
            #user_action = user_action.strip()
            # deze regels zouden er kunnen staan. Maar is repetitive code. Dat wil je niet.
            continue
            #continue is tegenovergestelde van break

    #case 'complete':
    #if 'complete' in user_action:
    #elif 'complete' in user_action:
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            #number = int(input("number of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
        continue

    #case 'exit':
    #if 'exit' in user_action:
    #elif 'exit' in user_action:
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print('Bye!')
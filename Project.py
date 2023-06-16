# password = input("Enter password: ")

# while password != "Pbob1":
#     password = input("Enter password: ")

# print("Password was correct!")
# _________________________________________________________
# x = 1

# while x <= 6:
#     print(x)
#     x = x + 1
import functions
import time

now = time.strftime('%b = %m %d, %Y %H:%M:%S')
print("It is", now)

while True:
    user_action = input("Type Add, Show, Edit, Complete or EXit: ")
    user_action = user_action.strip()
# -------------------------------------------------------------------------------ADD
#    match user_action:
#        case "add" | "a":
    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    #    message = f"Todo {todo} was added the list."
    #    print(message)
# ------------------------------------------------------------------------------SHOW
#        case "show" | "s":
    elif user_action.startswith('show'):

        todos = functions.get_todos()

#            new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos, 1):
            item = item.strip('\n')
            print(f"{index}. {item}")
        print(f"Length list is {index}")
# -------------------------------------------------------------------------------EDIT
#        case "edit" | "e":
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("your command is not valid.")
            continue
# -------------------------------------------------------------------------------DEL
#        case "complete" | "del" | "c":
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todoToRemove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todoToRemove} was removed from the list."
            print(message)
        except IndexError:  # error massege.
            print("There is no item with that number.")
            continue
# -------------------------------------------------------------------------------EXIT
#        case "exit" | "ex":
    elif user_action.startswith('exit') or user_action.startswith('ex'):
        break
    else:
        print("Command is not valid.")

print("Bye!")

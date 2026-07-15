#
# todos = []
#
# while True:
#     user_action = input("Type Add Or Show, or exit")
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo")
#             todos.append(todo)
#         case '':
#             print(todos)
#         case 'exit':
#             break
#
# print('bye!')


# #
# # todos = []
#
# while True:
#     user_action = input("Type Add Or Show, or exit")
#     user_action = user_action.strip()
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo")
#             todos.append(todo)
#         case 'show':
#             for item in todos:
#                 print(item)
#         case 'exit':
#             break
#         case x:
#             print('hey buddy try again')
#
# print('bye!')

#
# countries = []
#
# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
# print(countries)
#
# # countries = []
# #
# # while True:
# #     country = input("enter your country")
# #     countries.append(country)
# #     print(countries)

meals = ['pasta', 'pizza', 'salad']

for i in 'meals':
    print(i.capitalize())

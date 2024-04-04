pizza_list = []
user_input = ''
while(user_input != 'quit'):
    user_input = input("Enter a pizza topping:")
    if user_input != 'quit':
        print(f"ok, I'll add {user_input} to your pizza.\n")
        pizza_list.append(user_input)
pizza_list.append(user_input)

print(f"your pizza will have {len(pizza_list)} topping.")
for  user_input in pizza_list:
    print("    " + user_input)
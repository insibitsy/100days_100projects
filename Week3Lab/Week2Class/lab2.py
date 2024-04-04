number_of_quarters = int(input("Enter num of quarters: "))
number_of_dimes = int(input("Enter num of dimes: "))
number_of_nickels = int(input("Enter num of nickels: "))
number_of_pennies = int(input("Enter num of pennies: "))

total_money = (number_of_quarters * 0.25) + (number_of_dimes * 0.1) + (number_of_nickels * 0.05) + (number_of_pennies * 0.01)
print(f'You have ${total_money:.2f}')
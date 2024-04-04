import math
#amount = float(input("Enter a currency amount:"))
amount = 3.46
amount *=100
amount = int(amount)
#dollar = math.floor(currency)
#quarter = math.floor((currency - dollar) / .25)
#dime = math.floor((currency - (dollar + quarter)) / .10)
#print(dollar)
#print(quarter)
#print(dime)


dollars = amount // 100
#currency = currency % 1

amount %= 100
print(amount)
print(amount)

quarter = amount//25
amount %= 25

dimes = amount // 10
amount %= 10

nickels = amount // 5
amount %= 5

pennies = amount

print(amount)

print("Dollars:", dollars")
print("Quarters:", quarter")
print("Dimes:", dimes")
print("Nickels:", nickels")
print("Pennies:", pennies")
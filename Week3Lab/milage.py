milage = float(input("What is the gas milage of your car (in mpg):"))
gas_price = float(input("What is the cost of gas per gallon:"))


gas_cost = (20 / milage * gas_price)


print(f"if you drive {milage} miles, it will cost ${20 / milage * gas_price:.2f}")
print(f"if you drive {milage} miles, it will cost ${50 / milage * gas_price:.2f}")
print(f"if you drive {milage} miles, it will cost ${100 / milage * gas_price:.2f}")

print("Cost to drive:")
print("\tMiles\tCost")
print(f"\t20\t{20 / milage * gas_price:.2f}")
print(f"\t50\t{50 / milage * gas_price:.2f}")
print(f"\t100\t{100 / milage * gas_price:.2f}")
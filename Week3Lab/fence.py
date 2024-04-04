length_input = float(input("PLease enter the length of the plot: "))
width_input = float(input("PLease enter the width of the plot: "))

plot_area = length_input * width_input
plot_perm = (length_input * 2) + (width_input * 2)
fencing_cost = plot_perm * 20
print(f"The area of the plot is {plot_area} square meters.")
print(f"The perimeter of the plot is {plot_perm} square meters.")
print(f"The cost to fence the plot is ${fencing_cost}.")


input = int(input("Enter a number:"))
for i in range(2, input):
    if input % i == 0:
        print(f"{input} is not a prime number")
        break
else:
    print(f"{input} is a prime number")
grade = float(input("Enter your grade:"))

if grade >= 89.5:
    print(f"An {grade} is an A")
elif grade >= 80:
    print(f"An {grade} is an B")
elif grade >= 70:
    print(f"An {grade} is an C")
elif grade >= 60:
    print(f"An {grade} is an D")
elif grade >= 50:
    print(f"An {grade} is an F")
else:
    print("invalid entry")

print("grade entry complete")

if 89.5 < grade <= 115:
    print(f"An {grade} is an A")
elif 79.5 <+ grade <= 89.5:
    print(f"An {grade} is an B")
elif 69.5 <= grade <= 79.5:
    print(f"An {grade} is an C")
elif 59.5 <= grade <= 69.5:
    print(f"An {grade} is an D")
elif 0 <= grade <= 59.5:
    print(f"An {grade} is an F")  
else:
    print("invalid entry")
# Decode the US Interstate numbers. What highway numbers actually mean.

# "Primary" highways are numbered 1-99
# "Auxiliary" highways are numbered 100-999
#     The auxiliary highways service the primary highways indicated by the rightmost
#     two digits.
#     Ex: I-295 services I-95
#     Note: Numbers like 200, 300, etc are not valid numbers, 
#           because 00 is not a valid primary highway to service.
# Odd numbered highways go North/South
# Even numbered highways go East/West

# Ask the user to input a number
# Print the type of highway that number indicates.
# Ex:
#     Input: 90    Output: "I-90 is primary, going East/West."
#     Input: 290   Output: "I-290 is auxiliary, serving I-90, going East/West."
#     Input: 0     Output: "0 is not a valid interstate highway number."
#     Input: 200   Output: "200 is not a valid interstate highway number."
#   
print("\n\n")

number = 301

# is the number valid?
if (1 <= number <= 999) and (number % 100 != 0):
    if number < 100:
        # primary
        print(f"I-{number} is primary, ", end = "")
    else:
        # aux
        served = number % 100
        print(f"I-{number} is auxiliary, serving I-{served}, ", end = "")

    if number % 2 == 0: #even
        print("going East/West")
    else: #odd
        print("going North/South")


else:
    print(f"{number} is NOT a valid number for an interstate.")



print("\n\n")

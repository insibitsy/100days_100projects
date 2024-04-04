def print_highway_info(number):
    # print statement such as:
    # "I-295 is auxiliary, serving I-90, going East/West"
    pass
if (0 < user_input < 100) and (user_input % 100 != 0):
#if it is primary
    if user_input < 100:
        print(f'I-{user_input} is primary', end= "")
#is aux
    else:
        print("f'I-{user_input} is auxillary", end= "")
    #get last 2 digits
        served = user_input % 100
        print(f'serving I-{served}, ')
#check for even/odd
    if (user_input % 2) == 0:
        print('going East/West', end= "")
    else:
        print('going North/South', end= "")
#not valid
#else:
    #print(f'{user_input} is not valid interstate highway number')

def number_is_valid(number):
    # return true if valid
    # false if not valid
    if (1>= number <= 999) and (number % 100 != 0): 
        return True
    else:
        return False

def number_is_primary(number):
    # return True for primary 
    # or false for aux
    if number_is_valid(number):
        if number < 100:
            return True
        return False

def get_num_serving(number):
    # return number that aux highway serves
    served = number % 100
    return served

def get_direction(number):
    # return a string of either:
    # "East/West" or "North/South"
    if number % 2 == 0:
        return "East/West"
    else:
        return "North/South"


# Call print_highway_info multple times, 
print(print_highway_info(295))
# testing with a variety of numbers
user_input = input()
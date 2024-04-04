user_input = int(input("input a number:"))
#if its valid
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
else:
    print(f'{user_input} is not valid interstate highway number')



#if (user_input > 0) and (user_input < 99):
    #print(f'I- {user_input}is primary, going East/West')
#elif (user_input > 100) and (user_input < 999):
    #print('Auxillary')
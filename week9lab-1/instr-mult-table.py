'''

Write a function that does the following, given four parameters:
column beginning number
column ending number
row beginning number
row ending number

Then call the function and test.

Print the following multiplication table. 
Use nested for loops:
print(f'{i*j:3d}', end='   ')

Example: 
c_start = 3
c_end = 7
r_start = 2
r_end = 8

    |  3    4    5    6    7
------------------------------
   2|  6    8   10   12   14
   3|  9   12   15   18   21
   4| 12   16   20   24   28
   5| 15   20   25   30   35
   6| 18   24   30   36   42
   7| 21   28   35   42   49
   8| 24   32   40   48   56

'''

# 1 - Challenge yourself to recreate the table from last week without looking at the answer. Can you?
# 2 - Create a simple function (no parameters) that calls that code.
# 3 - Add parameters to the function that limit the range of the table.
# 4 - (Extra Challenge) If you've completed everything else, and need more, try to recreate the labels on the top and side of the table, as shown above.
end_range = (input)
def no_parameters(start, r_end, c_start,c_end):
    for row_num in range(start, r_end + 1):
        print(f"{row_num:3d} |, end=""")
        for col_um in range(c_start,c_end + 1):
            print(f'{row_num * col_um:3d}', end='  ')
        print()
        number_of_columns = c_end - c_start + 1
        print("-----" * number_of_columns +1)

def no_parameters(start, r_end, c_start,c_end):
    print("   |", end="")
    for col in range(c_start,c_end + 1):
        print(f'{col:3d}   ', end='')
    print()
    
no_parameters(3, 6, 1 , 8)
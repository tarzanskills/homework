def sum_of_natural_numbers(n):
    sum_start = 0
    for index in range(n):
        sum_start += index+1
    return sum_start

def sum_of_square_natural_number(n):
    sum_start = 0
    for index in range(n):
        sum_start += (index+1)**2
    return sum_start

def difference_function(a,b):
    return a-b

number = int(input("Enter number of natural numbers: "))
sum_of_squares = sum_of_square_natural_number(number)
sum_of_numbers = sum_of_natural_numbers(number)

# print(sum_of_squares)
# print(sum_of_numbers)

print("Difference between square of sum and sum of squares of the first", number, "natural numbers is", difference_function(sum_of_numbers**2,sum_of_squares))

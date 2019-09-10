def sum_of_digits(number):
    sum = 0
    while(number > 0):
        remainder = number % 10
        sum = sum + remainder
        number = number //10
    return sum

print (f"Sum of digits of 2^1000 is {sum_of_digits(2**1000)}")
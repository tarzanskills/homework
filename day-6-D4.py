def factorial(number):
    result = 1
    while number >= 1:
        result = result * number
        number = number - 1
    return result

def sum_of_digits(number):
    sum = 0
    while(number > 0):
        remainder = number % 10
        sum = sum + remainder
        number = number // 10
    return sum

input_number = int(input("Enter number to calculate sum of digits of its Factorial: "))
factorial_result = factorial(input_number)
print(f"Sum of digits of {input_number}! is {sum_of_digits(factorial_result)}") #sum_of_digits
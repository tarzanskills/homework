def number_of_digits(number):
    count = 0
    while(number > 0):
        number = number // 10
        count = count + 1
    return count

number_one = 0
number_two = 1
index = 2
while True:
    fibonacci_number = number_one + number_two
    digits = number_of_digits(fibonacci_number)
    if digits == 1000:
        break
    number_one = number_two
    number_two = fibonacci_number
    index += 1
print(index)
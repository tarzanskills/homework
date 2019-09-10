def prime_numbers(prime):
    is_prime = True
    for count in range(2,prime):
        if (prime%count == 0):
            is_prime = False
    return is_prime

for prime_range in range(2,30):
    if prime_numbers(prime_range):
        print (prime_range)



def sum_of_prime_digits(number):
    sum=0
    while number > 0:
        remainder= number % 10
        sum=sum + remainder
        number = number // 10
    return sum
sum_of_fact= sum_of_prime_digits(prime)


print(prime_numbers(prime))

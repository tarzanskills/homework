def prime_numbers(prime):
    is_prime = True
    for count in range(2,prime):
        if (prime%count == 0):
            is_prime = False
    return is_prime

for prime_range in range(2,30):
    if prime_numbers(prime_range):
        print (prime_range)



# vowels='a','i','o','e','u'
# input=str(input(""))
# input.casefold()
#  input.find==vowels
#     print('\n')
# else:
#     print("")

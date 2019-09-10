prime_count = 2
starting_number = 3



while prime_count <= 10001:
    for value in range (2, starting_number):
        is_prime = True
        if starting_number % value == 0:
            is_prime = False
            break

    if is_prime:
        prime_count = prime_count + 1
    starting_number = starting_number + 1

    print(prime_count)
print(starting_number)



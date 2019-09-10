numbers = 3
count = 2
while count <= 10001:
    isPrime = True
    for value in range (2, numbers):
        if numbers % value == 0:
            isPrime = False
            break
    if isPrime:
        count += 1
    print(count)
    if count <= 10001:
        numbers += 1
print (numbers)
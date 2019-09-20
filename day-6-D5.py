numbers = 3
sum = 2
while True:
    isPrime = True
    for value in range (2, numbers):
        if numbers % value == 0:
            isPrime = False
            break
    if isPrime:
        print (numbers)
        sum += numbers
    if numbers <= 20000:
        numbers += 1
    else:
        break
print (sum)
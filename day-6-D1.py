sum = 0
for value in range(1000):
    if value%3 == 0 and value%5 == 0:
        sum = sum + value
    print(sum)
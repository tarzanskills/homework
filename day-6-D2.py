first = 1
second = 2
result = 0
sum = 2

while first <= 4000000:
    result = first + second
    if result % 2 == 0:
        sum = sum + result

    first = second
    second = result

print(sum)
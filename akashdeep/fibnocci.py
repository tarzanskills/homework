def fibonacci_series(number):
    if number == 0 :
        return 0
    if number == 1:
        return 1
    else:
        return fibonacci_series(number-2)+fibonacci_series(number-1)


num = int(input("Enter a number:"))


for i in range(0 , num):
    print(fibonacci_series(i),end=" ")
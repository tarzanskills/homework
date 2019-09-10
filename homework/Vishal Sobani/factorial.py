
def factorial(number):

    if number<0:
        print()
    elif number==0:
        print("Print the numbers")
    else:
        for value in range(1,number+1):
            fact = fact * value

    sum = 0
    while number > 0:
        sum = sum + fact % 10
        fact = fact / 10

fact = 1
print("the factorial of a number is ",fact)

number=int(input("Enter the number "))
print(factorial(number))
print(sum)

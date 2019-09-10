
def factorial(number):
    fact = 1
    if number<0:
        print()
    elif number==0:
        print("Print the numbers")
    else:
        for value in range(1,number+1):
            fact = fact * value
        return fact

def sum_of_factorial(number):
    sum=0
    while number > 0:
        remainder= number % 10
        sum=sum + remainder
        number = number // 10
    return sum

number=int(input("Enter the number "))
print("the factorial of a number is ",factorial(number))
sum_of_fact= factorial(number)
print("SUm of digits in fact ", sum_of_factorial(sum_of_fact))


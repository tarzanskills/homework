import os
import sys
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def percentage(x, y):
    return  (x/y)*100

def memory_logs(value):
    foo = open("logs.txt","a+")
    foo.write('\n')
    foo.write(value)
    foo.close()

def view_logs():
    file_open = open("logs.txt","a+")
    file_open.seek(0, 0)
    print(file_open.read())
    file_open.close()

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Percentage")


cont = "y"
while cont.lower() == "y":

    choice = input("Enter choice(1/2/3/4/5):")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))


    if choice == '1':
        add1 = str(add(num1,num2))
        result = str("{0} + {1} = ".format(num1, num2) + add1)
        print("{0} + {1} = ".format(num1, num2) + add1)

    elif choice == '2':
         sub1 = str(subtract(num1,num2))
         result = str("{0} - {1} = ".format(num1,num2) + sub1)
         print("{0} - {1} = ".format(num1, num2) + sub1)

    elif choice == '3':
         mul1 = str(multiply(num1,num2))
         result = str("{0} * {1} = ".format(num1,num2) + mul1)
         print("{0} * {1} = ".format(num1,num2) + mul1)

    elif choice == '4':
        div1 = str(divide(num1,num2))
        result = str("{0} / {1} = ".format(num1,num2) + div1)
        print("{0} / {1} = ".format(num1,num2) + div1)

    elif choice == '5':
         per1 = str(percentage(num1,num2))
         result = str("{0} % {1} = ".format(num1,num2) + per1)
         print("{0} % {1} = ".format(num1,num2) + per1)

    else:
        print("Invalid input")

    memory_logs(result)




    cont = input("continue ? y/n: ")
    if cont == "n":
     break

view_logs()

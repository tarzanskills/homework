
#file_object =open('filehandling.txt','r')
#print(file_object.tell())

#file_write =open('fileHandling.txt','w')
#file_write.write("My name is Akash")

#file_read=open('filehandling.txt','r')
#file_read.read()

#file_append=open('filehandling.txt','a')
#file_append.write("lives in bangalore")

#file_binary=open('filehandling.txt',ab)
#file_object.close()

#file_read=open('filehandling.txt','r')
#print(file_read.read())


import os

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 -num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def percentage(num1, num2):
    return (num1 / num2) * 100

def add_memory(num1,num2,select):
    f_add_memory = open('filehandling.txt','r')
    mem_operation = str(num1)+str(num2)+str(select)
    f_add_memory.write(mem_operation)


def clear_memory():
    open('filehandling','w').close()


def view_memory():
    file_view_memory = open('filehandling','r')
    print(file_view_memory.read())


#print("select operation")
#print("1.add")
#print("2.subtract")
#print("3.multiply")
#print("4.Divide")
#print("5.percentage")

while True:
    select = input("Select operation")

    number_1 = int(input("Enter first number"))
    number_2 = int(input("Enter Second number"))

    if select == 'add':
        print(number_1, "+", number_2, "=", add(number_1, number_2))
    elif select == 'subtract':
        print(number_1, "-", number_2,"=",subtract(number_1,number_2))
    elif select == 'multiply':
        print(number_1,"*",number_2,"=",multiply(number_1,number_2))
    elif select == 'divide':
        print(number_1,"/",number_2,"=",divide(number_1,number_2))
    elif select == 'percentage':
        print("% of",number_1,"&",number_2,"=",percentage(number_1,number_2))
    elif select == 'add_memory':
        add_memory(number_1,number_2,select)
    elif select == 'view_memory':
        view_memory()
        continue

    elif select == 'clear_memory':
        clear_memory()
        break
    else:
        print("invalid input")
        break

# #Home Work
# my_full_name = "SAURABH NAYAK"
# print(my_full_name[:7])  #SAURABH
# print(my_full_name[8:])  #NAYAK
# print(my_full_name[::-1]) #REVERSE ORDER
# print(my_full_name[::2]) #Alternate character
# print(my_full_name[::-3])  #Alternate 2nd character in reverse
# print(my_full_name[6::-1])  #first name in reverse order
#
#
#
# def add(a,b):
#     return a+b
#
#
#
# print(add(3,4))
#
# first_name="varun"
# last_name="rathore"
#
# print(add(first_name, last_name))
#
#
# from decimal import Decimal
# print(add(Decimal('1.1'),Decimal('2.2')))
#
# from fractions import Fraction
# print(add(Fraction(3,4),Fraction(3,4)))
#
#
# first_value = int(input("Enter the value: "))
# second_value = int(input("Enter the value: "))
#
#
# print(add(first_value,second_value))
#
# def sub(a,b):
#     return a-b
#
# print(sub(45.0,20))
#
# a=87
# b=24
# print(sub(a,b))
# from decimal import Decimal
# from fractions import Fraction
# print(sub(Decimal('2.2'),Decimal('1.1')))
# print(sub(Fraction('2.3'),Fraction('24')))
#
#

my_string = input("Enter your name: ")

def rev(my_string):
    reversed = my_string[::-1]
    return reversed

my_reversed_name = rev(my_string)
print(f"My reversed name is : {my_reversed_name}")
print("My reversed name is :", my_reversed_name)



git c
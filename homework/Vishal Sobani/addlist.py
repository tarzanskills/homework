n=int(input("Enter the length of a list "))
a=[]
for i in range(0,n):
    array_num=int(input(f"Enter the {n} items :"))
    a.append(array_num)
average=sum(a)/n
print(f"Average of the items in list are {average}" )



first_num=int(input("Enter the value of first number "))
second_num=int(input("Enter the value of second number "))

first_num=first_num+second_num
second_num=first_num-second_num
first_num=first_num-second_num

print("......After reversing ")

print(f"first number : {first_num}")
print(f"second number : {second_num}")
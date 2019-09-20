side_a=int(input("Enter the input value for a: "))
side_b=int(input("Enter the input value for b:"))
side_c=int(input("Enter the input value for c :"))
if(side_a==side_b and side_b==side_c and side_c==side_a):
    print("This is equilateral triangle ")
elif(side_a==side_c or side_b==side_c or side_a==side_b):
    print("this is  issoscale triangle")
elif(side_a!=side_b and side_b!=side_c and side_c!=side_a):
    print(("This is scalene Triangle"))
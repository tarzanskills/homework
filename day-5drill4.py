side_1=int(input("enter the first side of triangle:"))
side_2=int(input("enter the second side of triangle:"))
side_3=int(input("enter the third side of triangle:"))
if side_1 == side_2 == side_3:
    print("The triangle is Equilateral")
elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
    print("The triangle is isoceles")
else:
    print("The triangle is Scalene")
print("Input lengths of the triangle sides:")
x = input("x: ")
y = input("y: ")
z = input("z: ")
if (x == y and y == z and x == z):
    print("Equilateral Triangle")
elif (x == y or y == z or z == x):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
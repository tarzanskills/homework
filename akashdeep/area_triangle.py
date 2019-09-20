def area_triangle(l,b,h):
    s=(l+b+h)/2
    area = (s*(s-l)*(s-b)*(s-h))**0.5
    return(area)

l = float(input("Enter lenght:"))
b = float(input("Enter base:"))
h = float(input("Enter height:"))

print(area_triangle(l,b,h))
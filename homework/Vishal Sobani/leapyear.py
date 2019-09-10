year=int(input("Enter the year "))

def leap(year):
    if year % 4 == 0 and year%100!=9 or year%400==0:
        print("it is a leap ")
    else:
        print("it is not leap year")
    return year

print (leap (year) )



def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year,"is a leap year.")
    else:
        print(year,"not a leap year")





year = int(input("Enter a Number:"))
print(leap_year(year))

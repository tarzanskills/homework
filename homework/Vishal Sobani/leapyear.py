check_year=int(input("Enter the year : "))

if check_year%4==0:
    if check_year%400==0:
        if check_year%100!=0:
            print("it is a leap year")
        else:
            print("not a leap year")
    else:
        print("it is a leap year")
else:
    print("it is not a leap")
from datetime import date
print ("Please enter your birthday ")
birth_year=str(input("Year:"))
birth_month=str(input("Month:"))
birth_day=str(input("Date:"))
now = date.today ()

age = date(str(birth_year), str(birth_month),str(birth_year))
print ("Your age is " + str(now-age))
print (int(now-age)*12)
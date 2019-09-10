from datetime import date

print ("Please enter your birthday ")

birth_year=int(input("Year:"))
birth_month=int(input("Month:"))
birth_day=int(input("Date:"))

now = date.today ()

age = date(int(birth_year), int(birth_month),int(birth_day))

print("Your age is " + str(now-age))
print((now-age)*60*60*24)
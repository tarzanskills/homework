#day 1 and day 2 drills

print("hello world!")
print("hello again!")
print("i like typing this")
print("yay printing")
print("I'd much rather you 'not'.")
print('I "said " do not touch this.')

###
print ("Please enter your birthday ")
bd_y=int(input("Year:"))
bd_m=int(input("Month (1-12):"))
bd_d=int(input("Date:"))

from datetime import date
now = date.today ()

age = date(int(bd_y), int(bd_m), int(bd_d))
print("Your age is " + str(now-age))
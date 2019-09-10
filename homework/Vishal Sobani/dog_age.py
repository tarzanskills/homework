input=int(input("Enter the age of dog's age in humar year "))

if input<=2:
    dog_age=input*10.5
else:
    dog_age=2*10.5 + 4 * (input -2)

print("the dog's age in years is ",dog_age)
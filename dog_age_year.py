human_years = int(input("Input a dog's age in human years: "))
if (human_years<=2):
    dogs_age = 10.5*human_years
else:
    dogs_age = 10.5*2 + 4*(human_years-2)
print("The dog's age in dog's years is", int(dogs_age))
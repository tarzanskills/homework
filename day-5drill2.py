input=int(input("Inputa  dog's age in human years: "))

if input<=2:
    dog_age=input*10.5
else:
    dog_age=2*10.5 + 4 * (input -2)

print("The dog's age in dog's years is ",dog_age)
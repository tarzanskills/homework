print(5>4)
print(3==5)
print(not(5>4))
print((5>4) or (3==5))
print(not((5>4) or (3==5)))
print((True and True) and (True==False))
print((not False) or (not True))

spam = int(input("Enter an integer: "))
if spam==1:
    print("Hello")
elif spam==2:
    print("Howdy")
else:
    print("Greetings!")
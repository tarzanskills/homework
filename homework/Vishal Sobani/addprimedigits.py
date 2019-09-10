number=int(input("Enter the range of prime numeber till want to add "))
sum=0
for value in range(0,number+1):
    if value>1:
        for prime in range(2,value):
            if(value%prime)==0:
                break
        else:
            sum=sum+value
        #print(value)

print(f"The sum of prime number upto {number} are",sum)
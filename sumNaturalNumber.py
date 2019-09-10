#input_number=int(input("Enter the input value : "))
#sum_of_Square=((input_number*(input_number+1))/2)**2
#print(sum_of_Square)
#square_of_number_sum=(input_number*(input_number+1)*(2*input_number+1))/6
#print(square_of_number_sum)
#print("The differance of them")
#differance=(sum_of_Square-square_of_number_sum)
#print(differance)
input_value=int(input("Enter the value : "))
start_value=1
sum_naturalNum=0
sum=0
while start_value<=input_value:
    square=start_value**2
    sum=sum+square
    sum_naturalNum=sum_naturalNum+start_value
    start_value += 1
sq_sumN=sum_naturalNum**2
diffrance=sq_sumN-sum

print(" square of N natural number sum",sum)
print(" sum of n natural number square is: ",sq_sumN)
print("Differance both of these ",diffrance)


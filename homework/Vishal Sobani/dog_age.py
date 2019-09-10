start_number=int(input("Enter the starting range of the series "))
end_number=int(input("Enter the end range of the series "))

sum_of_even=0
for value in range(start_number,end_number):
    if value%2==0:
        sum_of_even+=value
print(sum_of_even)


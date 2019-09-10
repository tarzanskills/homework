'''Find the sum of all the multiples of 3 or 5 below 1000'''

sum_val = 0
for i in range(1000):
    if (i % 3 == 0 or i % 5 == 0):
        sum_val = sum_val + i
        # the total val is print below.
print(sum_val)
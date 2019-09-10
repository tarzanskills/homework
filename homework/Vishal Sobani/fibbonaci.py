first_num=int(input("Enter an starting integer "))
second_num=int(input("Enter an ending integer "))
nterms = int(input("Number of terms "))
count = 0
even=0
if nterms <= 0:
   print("Please enter a positive integer ")
elif nterms == 1:
   print("Fibonacci sequence upto ",nterms)
   print(first_num)
else:
   print("Fibonacci sequence upto ",nterms)


while count < nterms:
       print(first_num,end=' ')
       nth_term = first_num + second_num
       first_num = second_num
       second_num = nth_term
       count += 1


"""To print the nth index of fibonnaci series"""

# start = 0
# end = 1
# list_length = []
# while True:
#     fib_series = start + end
#     start = end
#     end = nth_term
#     length = str(nth_term)
#     list_length.append(length)
#     if len(length) >= 1000:
#         print("Then index at 1000th is",len(list_length) + 1)
#         break

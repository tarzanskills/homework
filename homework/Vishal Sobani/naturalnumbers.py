
def sum_of_integers(number):

    sum = 0
    for value in range(1, number+1):
        sum = sum + (value * value)

    return sum

def square_of_integers(square):

    addition = 0
    for j in range (1, square+1):
        addition = addition + j
        square = addition ** 2
    return square

def diff_in_them(first_num,sec_num):

       return sec_num-first_num

number = int(input("Enter the integer "))
print(f"Sum of first {number} natural numbers are ",sum_of_integers(number))
print(f"Square of first {number} natural are ",square_of_integers(number))
print(f"Difference between {number} and {number} is ",diff_in_them(sum_of_integers(number),square_of_integers(number)))
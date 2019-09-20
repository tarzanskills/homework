nth_number = int(input("Enter the number : "))
print_count = 2
starting_number = 3
while print_count <= nth_number:
    for value in range(2, starting_number):
        is_Prime = True
        if starting_number % value == 0:
            is_Prime = False
            break
    if is_Prime:
        print_count += 1
    if print_count <= nth_number:
        starting_number += 1
print(starting_number)
length = int(input("Enter the side "))
for i in range(length):
    for j in range(length):

        if i == 0 or i == length - 1 or j == 0 or j == length - 1:
            print('4', end=' ')
        elif i == 1 or i == length - 1 or j == 1 or j == length - 1 and i+j == 7:
            print('3', end=' ')
        else:
            print('$',end = ' ')
    print()
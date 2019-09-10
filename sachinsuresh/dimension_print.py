dim = int(input("Enter dimensions: "))
for row in range(2*dim-1):
    print('\n')
    for col in range(2*dim-1):
        if(row>=dim):
            if(col>=dim):
                print(dim-min((2*dim-2)-row, (2*dim-2)-col), end=' ')
            else:
                print(dim-min((2*dim-2)-row,col), end = ' ')
        else:
            if(col>=dim):
                print(dim-min(row,(2*dim-2)-col), end = ' ')
            else:
                print(dim-min(row,col), end = ' ')
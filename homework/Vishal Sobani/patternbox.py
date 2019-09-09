def minimum_value(row_index,col_index):
    if row_index<=col_index:
        return row_index
    else:
        return col_index


dimension=int(input("Enter the dimension : "))
fact_1=2*dimension-1
fact_2=2*dimension-2
for row in range(fact_1):
    print()
    for col in range(fact_1):
        if row>=dimension:
            if col>=dimension:
                print(dimension-min((fact_2)-row,(fact_2)-col),end='')
            else:
                print(dimension-min((fact_2)-row,col),end='')
        else:
            if(col>=dimension):
                print(dimension-min(row,(fact_2)-col),end='')
            else:
                print(dimension-min(row,col),end='')

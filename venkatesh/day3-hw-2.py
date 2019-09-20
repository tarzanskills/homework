def add(a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)
    first_num = int(input("Enter your first_numb"))
    second_num = int(input("Enter your second_num"))
print("Choose operation","1:Add","2.Subtract","3.Multiply","4:Divide",sep="\n")
choice=input("choice operations from 1,2,3,4");


if choice == '1':
    print(first_num,"+", second_num,"=" ,add(first_num,second_num))


elif choice == '2':
    print(first_num ,"-" ,second_num ,"=" ,subtract(first_num,second_num))


elif choice == '3':
    print(first_num ,"*" ,second_num ,"=" ,multiply(first_num,second_num))


elif choice == '4':
    print(first_num ,"/", second_num, "=" ,divide(first_num,second_num))

else:
    print("Invalid")


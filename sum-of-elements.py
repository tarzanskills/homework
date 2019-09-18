n=int(input("enter the length of list:"))
list=[]
for i in range(n):
    elements = int(input("enter the elements:"))
    list.append(elements)
print("The elements in a list are:",list)

def sum(list1,n):
    if n == 0:
        return 0
    else:
        return list1[n-1] + sum(list1,n-1)

total = sum(list, len(list))

print("the sum of the list of elements:",total)
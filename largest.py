n=int(input("enter the length of list"))
list=[]
for i in range(n):
    items=int(input("enter the items:"))
    list.append(items)

print("Largest element in list is:",max(list))

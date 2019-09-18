n=int(input("Enter the length of a list:"))
list=[]
for i in range(n):
    elements=int(input("enter the elements:"))
    list.append(elements)
print(list)

def  occurence(list,item,i=0):
    item=int(input("enter the item to be checked in list:"))
    if i >= len(list):
        return False
    elif list[i] == item:
        return True
    else:
        return occurence(list,item,i+1)

occurence(elements)

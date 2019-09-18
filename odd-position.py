n=int(input("enter the length of list:"))
list=[]
odd_list=[]
count=0
for i in range(n):
    elements=int(input("enter the elemnts:"))
    list.append(elements)
print(list)

for i in list:
    if count % 2 == 1:
        odd_list.append(i)
    count += 1

print("the elements in odd positions of a list are",odd_list)

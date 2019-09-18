list=[1,2,4,6,7,10]
def reverse(list):
    if len(list) == 0:
        return []
    else:
        return [list.pop()] +reverse(list)
print("The original list is:",list)
print("Reverse of list is:",reverse(list))
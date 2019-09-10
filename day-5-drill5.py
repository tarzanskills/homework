first = 0
second = 1
count = 0
while count < 50:
    if count <= 1:
        Next = count
    else:
        Next = first + second
        first = second
        second = Next
    print (Next)
    count = count + 1
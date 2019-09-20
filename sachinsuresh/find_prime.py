import sys

value = 2
count = 0
while (value):

    if value == 2:
        count = count + 1
    elif value == 3:
        count= count + 1
    else:
        for index in range(2,(value//2)+1):
            passcode = True
            if (value%index) == 0:
                passcode = False
                break
        if passcode:
            count += 1
    if (count==10001):
        print(value)
        sys.exit()
    # print(count)
    value = value+1
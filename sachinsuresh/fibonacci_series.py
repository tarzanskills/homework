import sys

first = 0
second = 1
temp = 0

while(first>=0):
    temp = second
    second += first
    first = temp
    if (second>50):
        sys.exit()
    print(second)
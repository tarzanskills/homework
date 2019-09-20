first = int(input("value of a"))
second =int(input("value of b"))
third = int(input("value of c"))

def add(first,second):
    return (first+second+third)

def sub(second,third):
    return second-third

def multi(first,third):
    return (first*third)

def div(first,second):
    return (first/second)

print(add(first,second))
print(sub(second,third))
print(div(first,third))

REVERSING STRING

strng1=input("enter the str1")
strng2=input("enter the str2")
print(strng1[::-1])
print (strng2[::-1])

INCDLUDE SPACES

string4 = input("enter the strg")

def right_justify(string4):
    return(" "*(70-len(string4))+string4)

print(right_justify(string4))

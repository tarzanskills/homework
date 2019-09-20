# def create_memory1():
#     file_object=open('newfile.py','w')
#
#     file_object.close()
#
# print(create_memory1())
#
# def create_memory2():
#     file_boject=open('newfile.py','w')
#     file_boject.write('my name is pramod ray')
#     file_boject.close()
#
# print(create_memory2())
#
# def count_line():
#     file_boject = open('newfile.py', 'r')
#     print(file_boject.read(1))
#     file_boject.close()
#
#
# def count_line():
#     file_boject = open('newfile.py', 'r')
#     print(file_boject.read(1))
#     file_boject.close()


# n = int(input())
# for i in range(0, n):
#     j = i + 1
#     print(set(j))

import re
s = input()
# result = False
# for i in s:
#     if i.isalnum():
#         result = True
# print(result)
# result = False
# for i in s:
#     if i.isalpha():
#         result = True
# print(result)
#
# result = False
# for i in s:
#     if i.isdigit():
#         result = True
# print(result)
#
# result = False
# for i in s:
#     if i.islower():
#         result = True
# print(result)
#
# result = False
# for i in s:
#     if i.isupper():
#         result = True
# print(result)
if re.search('[a-zA-Z0-9]',s):
    print(True)
else:
    print(False)
if re.search('[A-Za-z]',s):
    print(True)
else:
    print(False)
if re.search('[0-9]',s):
    print(True)
else:
    print(False)
if re.search('[a-z]',s):
    print(True)
else:
    print(False)
if re.search('[A-Z]',s):
    print(True)
else:
    print(False)




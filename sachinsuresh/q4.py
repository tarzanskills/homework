#reverse contents of file

file_object = open("/home/sachin/tarzan/homework/sachinsuresh/Hello.txt", 'w')
text = 'hgvqwvqb'
num = '761614'
name = 'qifqk'
file_object.write(text)
file_object.write('\n')
file_object.write(num)
file_object.write('\n')
file_object.write(name)
file_object.close()

# s = open("/home/sachin/tarzan/homework/sachinsuresh/Hello.txt")
# string = s.read()
# print(string)
# l= string.split('\n')
# print(l)
# for line in reversed(list(open("/home/sachin/tarzan/homework/sachinsuresh/Hello.txt"))):
#     print(line.rstrip())

file_object = open("/home/sachin/tarzan/homework/sachinsuresh/Hello.txt", 'r')
string_read = file_object.read()
print(string_read[::-1])
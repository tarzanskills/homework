#number of lines of file

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

num_lines = sum(1 for line in open("/home/sachin/tarzan/homework/sachinsuresh/Hello.txt", 'r'))
print(num_lines)

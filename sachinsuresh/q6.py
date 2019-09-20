#compare contents of two files

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

fo = open("/home/sachin/tarzan/homework/sachinsuresh/Hi.txt", 'w')
text = 'hgvqwvqb'
num = '761614'
name = 'qifqk'
fo.write(text)
fo.write('\n')
fo.write(num)
fo.write('\n')
fo.write(name)
fo.close()

file_object = open("/home/sachin/tarzan/homework/sachinsuresh/Hello.txt", 'r')
string_file_1 = file_object.read()
fo = open("/home/sachin/tarzan/homework/sachinsuresh/Hi.txt", 'r')
string_file_2 = fo.read()

if (string_file_1==string_file_2):
    print("True")
else:
    print("False")
#open file in read mode copies bytes into another file

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

file_object = open("/home/sachin/tarzan/homework/sachinsuresh/Hello.txt", 'r')
string_text = file_object.read(2)
fo = open("/home/sachin/tarzan/homework/sachinsuresh/Hi.txt", 'w')
fo.write(string_text)
file_object.close()
fo.close()
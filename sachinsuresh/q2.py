#creates in w mode write input and print

file_object = open("/home/sachin/tarzan/homework/sachinsuresh/Hello.txt", 'w')
text = input("Enter your input: ")
file_object.write(text)
file_object.close()

file_object = open("/home/sachin/tarzan/homework/sachinsuresh/Hello.txt", 'r')
string_text = file_object.read()
print(string_text)
file_object.close()

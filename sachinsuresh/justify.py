def right_justify(s):
    string_length = len(s)
    print((" "*(70-string_length))+s)

string = input("Enter your string: ")
right_justify(string)
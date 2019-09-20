input_string=input("enter your string")
def right_justify(input_string):
    return(" "*(70-len(input_string))+input_string)

print(right_justify(input_string))


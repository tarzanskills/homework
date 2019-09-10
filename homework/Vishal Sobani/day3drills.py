def right_justify(input_string):
    lenth=len(input_string)
    print(" "*(70-lenth)+input_string)
    return input_string

input_string=input("enter ")
right_justify(input_string)

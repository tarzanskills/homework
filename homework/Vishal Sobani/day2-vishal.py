name=input("Enter the input ")
first_name=name.split()[0]
last_name = name.split()[2]
middle_name=name.split()[1]
reverse_firstname=first_name[::-1]
alt_char=name.split()[::2]
second_charcter_reverse=name[::-2]
name_in_rev=name[::-1]
middle_name_reverse=middle_name[::-1]
print(first_name)
print(middle_name)
print(last_name)
print(reverse_firstname)
print(alt_char)
print(name_in_rev)
print(middle_name_reverse)
print(second_charcter_reverse)


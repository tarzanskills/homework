# string_input=input("Enter the string value")
# for value in string_input:
#     if(value=='a' or value=='e' or value=='i'or  value=='o'or value=='u'):
#         print(value)
#     if(value!='a' or value!='e' or value!='i'or  value!='o'or value!='u'):
#         print(value)

string_input = input("enter a string: ")
vowel_string = ""
consonants_string = ""
for character in string_input:
    if (character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u'):
        vowel_string = vowel_string + character
    else:
        consonants_string = consonants_string + character
print (vowel_string)
print (consonants_string)


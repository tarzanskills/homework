# def print_vowels(string_name):
#     vowels = ""
#     for character in string_name:
#         if (character == 'a' or 'e' or 'i' or 'o' or 'u'):
#             vowels = vowels + character
#     print(character)
#
# def print_consonants(string_name):
#     consonants = ""
#     for character in string_name:
#         if (character != 'a' or 'e' or 'i' or 'o' or 'u'):
#             consonants = consonants + character
#     print(consonants)
#
# input_string = input("Enter the string: ")
# print_vowels(input_string)
# print_consonants(input_string)



vowels = 'aeiou'
s = 'pythonisamazing'

def check(s,vowels):
    only_v = [x for x in s if x in vowels]
    only_c = [x for x in s if x not in vowels]
    print('vowels in s:', "".join(only_v))
    print('conso in s:', "".join(only_c))

check(s,vowels)


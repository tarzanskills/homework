# ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
#         "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
#
# twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
#
# thousands = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ",
#              "septillion ", "octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ",
#              "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", "octodecillion ",
#              "novemdecillion ", "vigintillion "]
#
#
# def num999(n):
#     c = n % 10  # singles digit
#     b = ((n % 100) - c) // 10  # tens digit
#     a = ((n % 1000) - (b * 10) - c) // 100  # hundreds digit
#     t = ""
#     h = ""
#     if a != 0 and b == 0 and c == 0:
#         t = ones[a] + "hundred "
#     elif a != 0:
#         t = ones[a] + "hundred and "
#     if b <= 1:
#         h = ones[n % 100]
#     elif b > 1:
#         h = twenties[b] + ones[c]
#     st = t + h
#     return st
#
#
# def num2word(num):
#     if num == 0: return 'zero'
#
#     i = 3
#     n = str(num)
#     word = ""
#     k = 0
#     while (i == 3):
#         nw = n[-i:]
#         n = n[:-i]
#         if int(nw) == 0:
#             word = num999(int(nw)) + thousands[int(nw)] + word
#         else:
#             word = num999(int(nw)) + thousands[k] + word
#         if n == '':
#             i = i + 1
#         k += 1
#     return word[:-1]
#
#
# start_point = int(input("Enter the number start_point :"))
# sum = 0
# string_holder=""
# for value in range(start_point):
#     # sum = sum + start_point
#     string_holder += num2word(value)
#
#
# # string = sum_in_string.replace(' ', '', )
# # # string = sum_in_string.replace('-', '', )
# # string_count = len(string)
# print(len(string_holder))



# input_value1 = int(input("Enter the value : "))
# input_value2 = int(input("Enter the value : "))
#
# count=0
# rev=0
# sum1=0
# sum2=0
# sum3=0
#
# order_of_value1 =len(str(input_value1))
# order_of_value2=len(str(input_value2))
# while input_value1 > 0:
#    digit1 = input_value1 % 10
#    sum1 += digit1 ** order_of_value1
#    input_value1 //= 10
# while input_value2 > 0:
#    digit2 = input_value2 % 10
#    sum2+= digit2 ** order_of_value2
#    input_value1 //= 10
# sum_of_both=sum1+sum2
# order=len(str(sum_of_both))
# while sum_of_both > 0:
#     digit = input_value2 % 10
#     sum3 += digit ** order
#     input_value1 //= 10
# if sum3==sum_of_both :
#     print(sum3)









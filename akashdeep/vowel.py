def vowel_check(s):
    s = s.lower()
    if s == 'a' or s == 'e' or s == 'i' or s=='o' or s == 'u':
        print("vowel")
    else:
        print("consonant")


s = input("enter a string:")

print(vowel_check(s))

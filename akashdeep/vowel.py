def vowel_count(s):
    s = s.lower()
    count = 0
    for i in s:
        if i in "aeiou":
            return i
        print(i)



s = input("enter a string")
print(vowel_count(s))
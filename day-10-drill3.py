import re
def string(text):
    pattern="^\w+"
    if re.search(pattern,text):
        return("Match found")
    else:
        return("Not matched")

print(string("The Adventures of Batman"))
print(string("  The Adventures of Batman"))
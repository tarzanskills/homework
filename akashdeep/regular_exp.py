import re

password = input("Enter your password:")


def password_re(password):
    pattern = re.compile(r"a - zA - Z0 - 9){8, }")
    l_pattern = re.compile(r"a - z +")
    u_pattern = re.compile("A - Z +")
    digit_pattern = re.compile("[\d]) +")

    result = re.findall(pattern, password, l_pattern, u_pattern, digit_pattern)
    if pattern :
        print("Enter a strong password")
    elif l_pattern:
        print("Enter Valid Password")
    elif u_pattern:
        print("Enter valid password")
    elif digit_pattern:
        print("Enter valid password")
    else:
        print("password set successfully")


password_re(password)
def checkpassword(s):
    digit, lower, upper = 0, 0, 0
    for i in s:
        if i.isupper():
            upper = 1
        elif i.islower():
            lower = 1
        elif i.isdigit():
            digit = 1
    if upper and lower and digit: print("사용할 수 있습니다.")
    else: print("사용할 수 없습니다.")

checkpassword("abcA")
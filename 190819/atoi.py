def atoi(str):
    value = 0
    for i in range(len(str)):
        if ord(str[i]) >= ord('0') and ord(str[i]) <= ord('9'):
            digit = ord(str[i]) - ord('0')
        else:
            break
        value = (value * 10) + digit
    print(value)

print(type(atoi('123')))
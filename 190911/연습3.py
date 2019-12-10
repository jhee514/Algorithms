data = '0269FAC9A0'

def dec_bi():
    bi = {}
    for i in range(16):
        num = i
        temp = ''
        for j in range(3, -1, -1):
            temp += str(int(num) // (2**j))
            if int(num) // (2**j):
                num -= 2**j
        bi[i] = temp
    return bi

def hex_bi(data):
    bi = dec_bi()
    converted = ''
    for d in data:
        if d.isdigit():
            converted += bi[int(d)]
        else:
            converted += bi[ord(d) - ord("A") + 10]
    return converted

converted = hex_bi(data)
print("converted :", converted)


result = ''

patterns = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']


# TODO 암호는 중첩 되지 않는 점을 어케 잡아내지?
for c in range(len(converted)-1, -1, -1):
    print(c, end=' ')
    if converted[c] == '1':
        if converted[c-5:c+1] in patterns:
            result += str(patterns.index(converted[c-5:c+1])) + ', '


print()
print(result)
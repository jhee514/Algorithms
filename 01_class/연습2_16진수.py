def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1<<j) else '0'
    print(output)


raw = '01D06079561D79F99F'

# TODO 16진수 - 2진수 값을 저장한 리스트를 만들어서 값을 찾아오는 방식으로

def hex_bi(data):
    bi = {}
    for i in range(16):
        num = i
        temp = ''
        for j in range(3, -1, -1):
            temp += str(int(num) // (2 ** j))
            if int(num) // (2 ** j):
                num -= 2 ** j
        bi[i] = temp
    print(bi)
    converted = ''
    for d in data:
        if d.isdigit():
            converted += bi[int(d)]
        else:
            converted += bi[ord(d) - ord("A") + 10]
    return converted

print(hex_bi(raw))
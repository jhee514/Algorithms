raw_data = '0000000111100000011000000111100110000110000111100111100111111001100111'

data = [raw_data[i*7: (i+1)*7] for i in range(len(raw_data)//7)]

print(data)

output = ''

for d in data:
    total = 0
    for i in range(7):
        total += int(d[i])
        if i < 6:
            total = total * 2
    output += str(total) + ', '

print(output)
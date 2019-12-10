def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1<<j) else '0'
    print(output)

for i in range(-7, 8):
    print("%3d = " % i, end='')
    Bbit_print(i)

print()

a = 0x10
x = 0x01020304
print("%d = " % a, end='')
Bbit_print(a)
print()
print("0%X = " % x, end='')
for i in range(0, 4):
    Bbit_print((x >> i*8) & 0xff)

print()

n = 0x00111111
if n & 0xff:
    print("little endian")
else:
    print("big endian")

print()

aa = 0x86
key = 0xAA

print("aa      ==> ", end='')
Bbit_print(aa)

print("aa^=key ==> ", end='');
aa ^= key;
Bbit_print(aa)

print("aa^=key ==> ", end='');
aa ^= key;
Bbit_print(aa)
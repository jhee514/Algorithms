s = 'Reverse this strings'

ss = s[::-1]
print(ss)

ls = list(s)
ls.reverse()
print(''.join(ls))

for i in range(len(s) // 2):
    ls[i], ls[-1-i] = ls[-1-i], ls[i]
print(''.join(ls))
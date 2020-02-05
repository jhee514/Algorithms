text = "2+3*4/5"

op = ["*", "/", "+", "-"]
s = [0] * 100
nums = [0] * 100

top1 = 0
top2 = 0
for i in range(len(text)):
    if text[i] in op:
        s[top1] = text[i]
        top1 += 1
    else:
        nums[top2] = text[i]
        top2 += 1

print(''.join(nums[:top2]), ''.join(s[:top1][::-1]))
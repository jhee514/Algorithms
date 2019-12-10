def lomuto_prt(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def lumo_quick(data, l, r):
    if l < r:
        s = lomuto_prt(data, l, r)
        lumo_quick(data, l, s - 1)
        lumo_quick(data, s + 1, r)


data1 = [11, 45, 23, 81, 28, 34]
data2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
data3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
lumo_quick(data1, 0, len(data1) - 1)
lumo_quick(data2, 0, len(data2) - 1)
lumo_quick(data3, 0, len(data3) - 1)
print(data1)
print(data2)
print(data3)


def Hoare_partition(data, l, r):  # a는 list
    p = data[l]  # p : pivot
    i = l
    j = r
    while i < j:
        while i < r and data[i] <= p:
            i += 1
        while j > l and data[j] > p:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    data[l], data[j] = data[j], data[l]
    return j


def hoare_quick(data, l, r):
    if l < r:
        s = Hoare_partition(data, l, r)
        hoare_quick(data, l, s - 1)
        hoare_quick(data, s + 1, r)


data = [11, 45, 23, 81, 28, 34]
data4 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
data5 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
hoare_quick(data, 0, len(data) - 1)
hoare_quick(data4, 0, len(data4) - 1)
hoare_quick(data5, 0, len(data5) - 1)
print("Hoare")
print(data)
print(data4)
print(data5)

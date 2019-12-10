def SelectionSort(a):
    n = len(a)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[min], a[i] = a[i], a[min]



def SelectionSort_Recur(a, i=0):
    n = len(a)
    if i == n:
        return a

    # else:  # 없어도 된당
    min = i
    for j in range(i+1, n):
        if a[j] < a[min]:
            min = j
    a[min], a[i] = a[i], a[min]
    # i += 1  # 밑에 함수 호출할 때 i+1 로 호출하면 된다
    SelectionSort_Recur(a, i+1)


a = [1, 3, 6, 78, 4, 86, 214, 653, 2, 9, 21]
SelectionSort(a)
print(a)
aa = [1, 3, 6, 78, 4, 86, 214, 653, 2, 9, 21]
SelectionSort_Recur(aa)
print(aa)
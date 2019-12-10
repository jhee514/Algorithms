def Counting_Sort(A, B, k):
    C = [0] * k

    for i in range(0, len(B)):
        C[A[i]] += 1  # C[0] = 1, C[4] = 1, 각각 값을 count

    for i in range(1, len(C)):
        C[i] += C[i-1]  # counting 누적

    for i in range(len(B)-1, -1, -1):  # i in range(4, -1, -1)
        B[C[A[i]]-1] = A[i]  # B[C[A[4]]-1] == B[C[1]-1] == B[2] = A[4]
        C[A[i]] -= 1


A = [0, 4, 1, 3, 1, 2, 4, 1]
B = [0] * len(A)
Counting_Sort(A, B, len(set(A)))

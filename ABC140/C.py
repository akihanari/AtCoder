# coding: utf-8
N = int(input())
B = list(map(int, input().split()))
A = B
A.insert(0, B[0])
for i in range(1, N - 1):
    if A[i] > A[i+1]:
        A[i] = A[i+1]
print(sum(A))

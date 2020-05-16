# coding: utf-8
N, M = map(int, input().split())
for i in range(N):
    if i == 0:
        K = list(map(int, input().split()))
        K = set(K[1:])
    else:
        A = list(map(int, input().split()))
        A = set(A[1:])
        K = K & A
print(len(K))

# coding: utf-8
N, M = map(int, input().split())
A = [0 for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    A[a - 1] += 1
    A[b - 1] += 1
for i in A:
    print(i)

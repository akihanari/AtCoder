# coding: utf-8
N, M, C = map(int, input().split())
B = list(map(int, input().split()))

c = 0
for i in range(N):
    A = list(map(int, input().split()))
    tmp = [A[i]*B[i] for i in range(M)]
    if sum(tmp, C) > 0:
        c += 1
print(c)

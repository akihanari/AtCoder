# coding: utf-8
N = int(input())
P = list(map(int, input().split()))
minn = 1
c = 0
for i in range(N):
    if minn > P[i] or i == 0:
        minn = P[i]
        c += 1
print(c)

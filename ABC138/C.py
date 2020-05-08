# coding: utf-8
N = int(input())
v = list(map(int, input().split()))
v.sort()
ans = 0
i = 0
while i < N - 1:
    v[i+1] = (v[i] + v[i+1]) /2
    i += 1
print(v[N-1])

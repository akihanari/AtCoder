# coding: utf-8
import itertools

N, M, Q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(Q)]
l = [i for i in range(1, M + 1)]
A = list(itertools.combinations_with_replacement(l, N))

maxans = 0

for j in A:
    ans = 0
    for i in lst:
        if j[i[1]-1] - j[i[0]-1] == i[2]:
            ans = ans + i[3]
    maxans = max(maxans, ans)

# coding: utf-8
import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
c = 1
pn = 0
qn = 0
lst = [i for i in range(1, N+1)]
for i in itertools.permutations(lst, N):
    if i == P:
        pn = c
    if i == Q:
        qn = c
    c += 1
print(abs(pn - qn))

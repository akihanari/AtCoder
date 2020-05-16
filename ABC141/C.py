# coding: utf-8
import collections
N, K, Q = map(int, input().split())
A = [int(input()) for i in range(Q)]
# print(A)
c = collections.Counter(A)
# print(c)
for i in range(1, N+1):
    if K - Q + c[i] >= 1:
        print('Yes')
    else:
        print('No')

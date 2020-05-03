# coding: utf-8
N, K = map(int, input().split())
a = []
for i in range(K):
    d = int(input())
    a += list(map(int, input().split()))
a = set(a)
b = set(i for i in range(1, N+1))

print(len(a ^ b))

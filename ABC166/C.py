# coding: utf-8
N, M = map(int, input().split())
H = list(map(int, input().split()))

lst = [1 for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    if H[A-1] <= H[B-1]:
        lst[A-1] = 0
    if H[B-1] <= H[A-1]:
        lst[B-1] = 0

print(sum(lst))

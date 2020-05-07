# coding: utf-8
N = int(input())
A = list(map(int, input().split()))

lst = [0 for i in range(N)]
for i in range(N):
    lst[A[i]-1] = i+1

print(' '.join(map(str, lst)))

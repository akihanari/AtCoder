# coding: utf-8
N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

i = 0
A = 0
B = 0
while i < N:
    A += a[i]
    if i+1 < N:
        B += a[i+1]
    i += 2
print(A - B)

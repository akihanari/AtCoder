# coding: utf-8
A, B, C, D = map(int, input().split())

while not(A <= 0 or C <= 0):
    C -= B
    if C <= 0:
        print('Yes')
        break
    A -= D
    if A <= 0:
        print('No')
        break

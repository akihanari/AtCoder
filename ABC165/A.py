# coding: utf-8
K = int(input())
A, B = map(int, input().split())
lst = [i % K for i in range(A, B + 1)]
if 0 in lst:
    print('OK')
else:
    print('NG')

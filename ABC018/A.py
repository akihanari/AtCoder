# coding: utf-8
A = int(input())
B = int(input())
C = int(input())
lst = [A, B, C]
lst.sort(reverse=True)
print(lst.index(A) + 1)
print(lst.index(B) + 1)
print(lst.index(C) + 1)

# coding: utf-8
A = [int(input()) for i in range(5)]
B = [10 if i % 10 == 0 else i % 10 for i in A]
minB = A.pop(B.index(min(B)))
A = [i if i % 10 == 0 else i + 10 - (i % 10) for i in A]
A.append(minB)
print(sum(A))

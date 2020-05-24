# coding: utf-8
A = list(map(int, input().split()))
# print(A)
A.sort()
# print(A)
ans = abs(A[1] - A[0]) + abs(A[2] - A[1])
print(ans)

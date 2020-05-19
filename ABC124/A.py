# coding: utf-8
A, B = map(int, input().split())
# print(A, B)
M = max(A, B)
N = min(A, B)
# print(M)
if abs(A - B) >= 1:
    ans = M + (M - 1)
else:
    ans = M + N
print(ans)

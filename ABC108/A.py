# coding: utf-8
K = int(input())
# print(K)
if K % 2 == 0:
    ans = K // 2 * K // 2
else:
    ans = (K + 1) // 2 * (K - 1) // 2
print(ans)

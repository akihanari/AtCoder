# coding: utf-8
A, B, N = map(int, input().split())

num = min(B-1, N)

print(A * num // B - A * (num // B))
# tmp = 0
# ans = 0
# for i in range(1, N+1):
#     tmp = math.floor(A * i / B) - A * math.floor(i / B)
#     print("tmp:",i, tmp, math.floor(A * i / B), A * math.floor(i / B))
#     if ans < tmp:
#         x = i
#     ans = max(tmp, ans)
# print(ans, x)

# coding: utf-8
N = int(input())
ans = 0
for i in range(1, N+1):
    tmp = i
    num = 0
    while tmp % 2 == 0:
        num += 1
        tmp = tmp // 2
    ans = max(ans, num)
print(2**ans)

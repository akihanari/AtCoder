# coding: utf-8
N = int(input())
a = list(map(int, input().split()))
num = 0
for i in range(N):
    if a[i] == num + 1:
        num += 1
if num == 0:
    print(-1)
else:
    print(N - num)

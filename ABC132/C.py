# coding: utf-8
N = int(input())
d = list(map(int, input().split()))
d.sort()
m = d[N//2-1]
if m != d[N//2]:
    print(d[N//2] - m)
else:
    print(0)

# coding: utf-8
lst = list(map(int, input().split()))

K = lst[3]
c = 0
a = 0

for i in range(3):
    if K > 0:
        a = min(lst[i], K)
        K = K - a
        if i == 0:
            c += a * 1
        elif i == 2:
            c += a * (-1)
    else:
        break
print(c)

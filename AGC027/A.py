# coding: utf-8
N, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if sum(a) == x:
    print(N)
else:
    c = 0
    for i in a:
        if i > x:
            break
        x -= i
        c += 1
    if c == N:
        print(c - 1)
    else:
        print(c)

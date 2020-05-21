# coding: utf-8
N, A, B = map(int, input().split())
s = 0
for i in range(1, N+1):
    n = i
    m = 0
    while n > 9:
        m += n % 10
        n = n // 10
    m += n
    if A <= m <= B:
        s += i
print(s)

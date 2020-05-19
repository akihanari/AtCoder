# coding: utf-8
S = input()
N = len(S)


def create(N, b, c):
    a = ""
    i = 0
    while i < (N // 2):
        a += b + c
        i += 1
    if N % 2 == 1:
        a += b
    lst = [0 for i in range(N) if a[i] == S[i]]
    return len(lst)


print(min(create(N, '1', '0'), create(N, '0', '1')))

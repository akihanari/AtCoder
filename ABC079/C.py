# coding: utf-8
A = list(input())
for i in range(2 ** 3):
    op = ["-"] * 3
    for j in range(3):
        if ((i >> j) & 1):
            op[3 - 1 - j] = "+"
    ans = ""
    for m, n in zip(A, op):
        ans += m + n
    ans += A[3]
    if eval(ans) == 7:
        print(ans + "=7")
        exit()

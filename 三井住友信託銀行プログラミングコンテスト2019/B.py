# coding: utf-8
import math
N = int(input())

ans = int(N // 1.08 + 1)

if N == int(ans * 1.08):
    print(ans)
else:
    print(":(")

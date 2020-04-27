# coding: utf-8
a = int(input())
b = int(input())
ans = a % b
if a % b != 0:
    print(b - ans)
else:
    print(ans)

# coding: utf-8
import math
X = int(input())
num = 0
ans = 100

while ans < X:
    ans += math.floor(ans * 0.01)
    num += 1
print(num)

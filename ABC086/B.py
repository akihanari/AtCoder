# coding: utf-8
import math
a, b = input().split()
tmp = int(a+b)
ans = int(math.sqrt(tmp))
if ans*ans == tmp:
    print('Yes')
else:
    print('No')

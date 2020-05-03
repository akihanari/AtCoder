# coding: utf-8
import math
A, B = map(int, input().split())
if B == 1:
    print(0)
elif B - A > 0:
    num = 1
    B = B - A
    print(num + math.ceil(B/(A-1)))
else:
    print(1)

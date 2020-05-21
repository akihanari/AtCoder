# coding: utf-8
H = int(input())
c = 0
n = 0
while H > 1:
    c += 1
    H = int(H / 2)
print(2 **(c + 1) - 1)

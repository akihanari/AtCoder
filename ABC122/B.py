# coding: utf-8
S = input()
c = 0
m = 0
for i in S:
    if 'A' == i or 'C' == i or 'G' == i or 'T' == i:
        c += 1
        m = max(c, m)
    else:
        c = 0
print(m)

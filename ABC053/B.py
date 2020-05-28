# coding: utf-8
s = input()
m = -1
for i in range(len(s)):
    if s[i] == 'A' and m == -1:
        m = i
    elif s[i] == 'Z' and m != -1:
        n = i - m + 1
print(n)

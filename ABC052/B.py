# coding: utf-8
N = int(input())
S = input()
x = 0
c = 0
for i in range(N):
    if S[i] == 'I':
        x += 1
    else:
        x -= 1
    c = max(c, x)
print(c)

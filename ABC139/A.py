# coding: utf-8

S = input()
T = input()
# print(S, T)

c = 0

for i in range(3):
    if S[i] == T[i]:
        c += 1
print(c)

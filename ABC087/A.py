# coding: utf-8
X = int(input())
A = int(input())
B = int(input())

ans = (X - A) // B
ans = X - A - B * ans
print(ans)

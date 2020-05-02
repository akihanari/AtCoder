# coding: utf-8
N = int(input())
num = 10000
lst = [num * i / N for i in range(1, N + 1)]
print(sum(lst))

# coding: utf-8
N, M, X = map(int, input().split())
A = list(map(int, input().split()))
lst = [1 if (i in A) else 0 for i in range(1, N+2)]
lst2 = lst[:X]
lst3 = lst[X-1:]
print(min(sum(lst2),sum(lst3)))

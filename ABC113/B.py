# coding: utf-8
N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
lst = []
for i in H:
    ans = abs(A - (T - i * 0.006))
    lst.append(ans)
print(lst.index(min(lst))+1)

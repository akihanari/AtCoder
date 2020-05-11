# coding: utf-8
N = int(input())
D, X = map(int, input().split())
ans = X
for i in range(N):
    A = list(range(1, D+1, int(input())))
    ans += len(A)
print(ans)

# coding: utf-8
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
c = 0
for i in range(N):
    for j in range(N):
        if i != j:
            dis = sum([abs(a - b)** 2 for a, b in zip(X[i], X[j])])**0.5
            if dis.is_integer() == True:
                c += 1
print(c//2)

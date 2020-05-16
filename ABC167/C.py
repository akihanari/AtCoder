# coding: utf-8
N, M, X = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]
n = len(C)
m = -1
for i in range(2 ** n):
    A = [0 for i in range(M+1)]
    total = 0
    for j in range(n):
        if((i >> j) & 1):
            A = [a + b for a, b in zip(A, C[j])]
            B = [k for k in range(1, M+1) if A[k] < X]
            if len(B) == 0:
                if m == -1:
                    m = A[0]
                else:
                    m = min(m, A[0])
                break
print(m)

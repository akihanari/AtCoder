# coding: utf-8
A, B, C = map(int, input().split())
count = 0

while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    if A == B == C:
        print(-1)
        exit()
    count += 1
    A1 = A
    B1 = B
    C1 = C
    A = B1//2 + C1//2
    B = A1//2 + C1//2
    C = A1//2 + B1//2

print(count)

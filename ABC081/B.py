# coding: utf-8
N = int(input())
A = list(map(int, input().split()))
c = 0
# print(N)
# print(A)
while True:
    A = [i // 2 if i % 2 == 0 else "*" for i in A]
    # print(A)
    if "*" in A:
        break
    c += 1
print(c)

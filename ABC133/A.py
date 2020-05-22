# coding: utf-8
N, A, B = map(int, input().split())
# print(N, A, B)

train = N * A
taxi = B
print(min(train, taxi))

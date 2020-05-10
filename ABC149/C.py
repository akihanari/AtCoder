# coding: utf-8
import math


def prime(X):
    if X == 1:
        return False

    for i in range(2, int(math.sqrt(X)) + 1):
        if X % i == 0:
            return False
    return True


X = int(input())
while prime(X) == False:
    X += 1
print(X)

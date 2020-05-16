# coding: utf-8
a, b = map(int, input().split())

if a <= 0 and b >= 0:
    print("Zero")
elif b < 0 and (a - b) % 2 == 0:
    print("Negative")
else:
    print("Positive")

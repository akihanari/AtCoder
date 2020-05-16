# coding: utf-8

a = list(int(input()) for i in range(5))
k = int(input())

# print(a, k)
for i in range(5):
    for j in range(4):
        if a[j + 1] - a[i] > k:
            print(':(')
            exit()
else:
    print('Yay!')

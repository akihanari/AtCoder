# coding: utf-8
N = int(input())
for i in range(N):
    num = input()
    lst = [num[i] + (len(num) - i - 1)*'0' for i in range(len(num)) if num[i] != '0']
    print(len(lst))
    print(' '.join(lst))

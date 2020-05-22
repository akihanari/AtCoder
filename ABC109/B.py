# coding: utf-8
N = int(input())
lst = [input() for i in range(N)]
for i in range(N-1):
    n = lst[i]
    m = lst[i+1]
    if lst[i+1] in lst[:i+1] or n[-1] != m[0]:
        print('No')
        exit()
print('Yes')

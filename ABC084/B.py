# coding: utf-8
A, B = map(int, input().split())
S = input()
for i in range(len(S)):
    if i == A:
        if S[i] != '-':
            print('No')
            exit()
    else:
        if not ('0' <= S[i] <= '9'):
            print('No')
            exit()
else:
    print('Yes')

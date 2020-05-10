# coding: utf-8
S = input()
T = input()
if S in T:
    if (len(S) == len(T) - 1) and T.index(S) == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')

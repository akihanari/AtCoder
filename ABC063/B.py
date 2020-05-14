# coding: utf-8
S = input()
if len(S) != len(set(S)):
    print('no')
else:
    print('yes')

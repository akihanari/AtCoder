# coding: utf-8
N = input()
A = ['2', '4', '5', '7', '9']
B = ['0', '1', '6', '8']
if N[-1] in A:
    print('hon')
elif N[-1] in B:
    print('pon')
elif N[-1] == '3':
    print('bon')

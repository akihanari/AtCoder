# coding: utf-8
N, A, B = map(int, input().split())
S = input()
num = 0
fo = 0
for i in range(N):
    if num >= A + B or S[i] == 'c':
        print('No')
    elif S[i] == 'a':
        print('Yes')
        num += 1
    elif S[i] == 'b':
        fo += 1
        if fo <= B:
            print('Yes')
            num += 1
        else:
            print('No')
   

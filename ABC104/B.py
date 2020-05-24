# coding: utf-8
S = input()
if S[0] == 'A' and 'C' in S[2:-1] and S[1:S.find('C')].islower() is True and S[S.find('C')+1:].islower() is True:
    print('AC')
else:
    print('WA')

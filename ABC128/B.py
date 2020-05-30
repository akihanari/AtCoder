# coding: utf-8
N = int(input())
lst = []
for i in range(N):
    SP = list(map(str, input().split()))
    SP.append(i+1)
    lst.append(SP)

lst.sort(key=lambda x:(x[0],-int(x[1])))

for i in range(N):
    print(lst[i][2])

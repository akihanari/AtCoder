# coding: utf-8
s = int(input())
i = s
a = [s]
while True:
    if (i)%2 == 0:
        i = i//2
    else:
        i = 3*(i) + 1
    if i in a:
        print(len(a)+1)
        exit()
    a.append(i)

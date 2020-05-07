# coding: utf-8
import collections

S = input()
# print(S)
c = collections.Counter(S)
# print(c)

if len(S) == 4 and (c.most_common()[0][1] == 2 and c.most_common()[1][1] == 2):
    print("Yes")
else:
    print("No")

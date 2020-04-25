# %% [markdown]
# 日立製作所 社会システム事業部 プログラミングコンテスト2020

# %% [markdown]
# A - Hitachi String

# In[]:
S = input()
#print("S:", S)
while len(S) > 0:
    # vprint("S[:2]", S[:2])
    if S[:2] != 'hi':
        print('No')
        exit()
    S = S[2:]
    # print(":", S)
print('Yes')


# %% [markdown]
# B - Nice Shopping

# In[]:
# coding: utf-8
A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = sorted(a)
b1 = sorted(b)
z = [list(map(int, input().split())) for _ in range(M)]

num1 = a1[0] + b1[0]
# print("num1:", num1)
for i in range(M):
    x, y, c = z[i]
    num = a[x - 1] + b[y - 1] - c
    if num < num1:
        num1 = num
print(num1)


# %% [markdown]
# C - ThREE

# %% [markdown]
# パナソニックプログラミングコンテスト2020
# A - Kth Term

# In[]:
X = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
K = int(input())

print(X[K - 1])

# %% [markdown]
# B - Bishop

# In[]:
# coding: utf-8

H, W = map(int, input().split())
# print(H, W)

N = int(H * W / 2)
# print(int(N))
if H == 1 or W == 1:
    print(1)
elif H * W % 2 != 0:
    print(N + 1)
else:
    print(N)

# %% [markdown]
# C - Sqrt Inequality

# In[]:
# coding: utf-8

a, b, c = map(int, input().split())
# print(a, b, c)

if 0 < c - a - b and 4 * a * b < (c - a - b)**2:
    print('Yes')
else:
    print('No')

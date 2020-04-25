# %% [markdown]
# A - Station and Bus

# In[]:
S = input()
print("S:", S)
if ('A' in S) and ('B' in S):
    print("Yes")
else:
    print("No")

# %% [markdown]
# B - Count Balls

# In[]:
# coding: utf-8
N, A, B = map(int, input().split())
# print("N:", N, "A:", A, "B:", B)
if A == 0:
    print(0)
elif B == 0 or N <= A:
    print(N)
else:
    num = int(N / (A + B)) * A + min(A, N % (A + B))
    print(num)

# %% [markdown]
# C - Tax Increase

# In[]:
# coding: utf-8
import math
A, B = map(int, input().split())
# print("A:", A, "B:", B)

for i in range(1, 1010):
    if math.floor(i * 0.08) == A and math.floor(i * 0.1) == B:
        print(i)
        exit()
print(-1)

# %% [markdown]
# D - String Formation

# In[]:
# coding: utf-8
S = input()
Q = int(input())
# print("S:", S, "Q:", Q)

lst = [input() for _ in range(Q)]
# print("lst:", lst)
flg = True
# print("S:", S)
left = ""
right = ""
for i in lst:
    if i[0] == '1':
        flg = not flg
    else:
        if flg == False:
            if i[2] == '1':
                right = right + i[4]
                # print("right:", right)
            else:
                left = i[4] + left
                # print("left:", left)
        else:
            if i[2] == '1':
                left = i[4] + left
                # print("left:", left)
            else:
                right = right + i[4]
                # print("right:", right)
S = left + S + right
if flg == False:
    print(S[::-1])
else:
    print(S)

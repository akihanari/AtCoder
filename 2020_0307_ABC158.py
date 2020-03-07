# %% [markdown]
# In[]:
# A - Station and Bus

S = input()
print("S:", S)
if ('A' in S) and ('B' in S):
    print("Yes")
else:
    print("No")

# %% [markdown]
# B - Count Balls

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

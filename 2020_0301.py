# %% [markdown]
# **ABC157**<br>
# **A - Duplex Printing**<br>

# In[]:
N = int(input())
if N % 2 == 0:
    print(N // 2)
else:
    print((N // 2) + 1)


# %% [markdown]
# **B - Bingo**<br>

# In[]:

def cal(lst1, lst2):
    lst3 = [0, 0, 0]
    for i in range(3):
        if lst1[i] in lst2:
            lst3[i] = 1
    return lst3

def judge(a, b, c):
    if (a == 1) and (a == b == c):
        return True
    else:
        return False

A_1 = list(map(int, input().split()))
A_2 = list(map(int, input().split()))
A_3 = list(map(int, input().split()))
# print("A_1:", A_1)
# print("A_2:", A_2)
# print("A_3:", A_3)
N = int(input())
b = [int(input()) for _ in range(N)]

C_1 = []
C_2 = []
C_3 = []

C_1 = cal(A_1, b)
C_2 = cal(A_2, b)
C_3 = cal(A_3, b)
# print("C_1", C_1)
# print("C_2", C_2)
# print("C_3", C_3)

# 縦
a = judge(C_1[0], C_2[0], C_3[0])
b = judge(C_1[1], C_2[1], C_3[1])
c = judge(C_1[2], C_2[2], C_3[2])

# 横
d = judge(C_1[0], C_1[1], C_1[2])
e = judge(C_2[0], C_2[1], C_2[2])
f = judge(C_3[0], C_3[1], C_3[2])

g = judge(C_1[0], C_2[1], C_3[2])
h = judge(C_1[2], C_2[1], C_3[0])

lst = [a, b, c, d, e, f, g, h]

if True in lst:
    print('Yes')
else:
    print('No')

# %% [markdown]
# **C - Guess The Number 結果:WA**<br>

# In[]:
import re

N, M = map(int, input().split())
# print("N:", N, "M:", M)
s = [list(map(int, input().split())) for _ in range(M)]
s.sort()
# print(s)

c = []
for i in range(N):
    c.append('x')

for i in s:
    # print("c:", c, " i:", i, " c[i[0] - 1]:", c[i[0] - 1])
    # if i[0] - 1 == 0 and i[1] == 0:
    #   pass
    if (c[i[0] - 1] == 'x') or (c[i[0] - 1] > i[1]):
        c[i[0] - 1] = i[1]

c = map(str, c)

d = ''.join(c)
# print("d:", d)
d = re.sub('x', '0', d)
# print("d:", d)
if (d[:1] == "0") and (N != 1):
    print("-1")
else:
    print(d)

# %% [markdown]
# **C - Guess The Number 再チャレンジ結果:AC**<br>
N, M = map(int, input().split())
# print("N:", N, "M:", M)
s = [list(map(int, input().split())) for _ in range(M)]
# print(s)

c = []
for i in range(N):
    c.append(0)
flg = True
for i in s:
    if i[0] - 1 == 0 and i[1] == 0 and N != 1:
        flg = False
        break
    if (c[i[0] - 1] != 0) and c[i[0] - 1] != i[1]:
        flg = False
        break
    c[i[0] - 1] = i[1]

c = map(str, c)
d = ''.join(c)

if flg == False:
    print("-1")
elif (d[:1] == "0") and (N != 1):
    print("1" + d[1:])
else:
    print(d)

# In[]:

# In[]:

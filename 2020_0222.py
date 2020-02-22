# %% [markdown]
# **ABC085C - Otoshidama**<br>

# In[]:
# 提出結果:WA
# N枚のお札の合計金額がY円となることがありえるか
def num_judge(n, Y, N):
    if int(Y / n) > N:
        max = N
    else:
        max = int(Y / n)
    return max

N, Y = map(int, input().split())

Y = int(Y / 1000)

x_max = num_judge(10, Y, N)
y_max = num_judge(5, Y, N)

x = 0
flg = 0

while x <= x_max:
    y = 0
    while y <= y_max:
        z = N - (x + y)
        if (z >= 0) and (x * 10 + y * 5 + z == Y):
            print(x, y, z)
            flg = 1
            break
        y += 1
    if flg == 1:
        break
    x += 1
else:
    print(-1, -1, -1)
# In[]:

# In[]:

# In[]:

# In[]:

# In[]:

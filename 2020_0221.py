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
print("N:", N, "Y:", Y)

x = 0
y = 0
z = 0
flg = 0
# print (x, y, z)
Y = int(Y / 1000)
print("Y:", Y)

x_max = num_judge(10, Y, N)
y_max = num_judge(5, Y, N)
z_max = num_judge(1, Y, N)
print("x_max:", x_max, "y_max:", y_max, "z_max:", z_max)
while z <= z_max:
    y = 0
    while y <= y_max:
        x = 0
        while x <= x_max:
            if x + y + z > N:
                pass
            elif (x * 10 + y * 5 + z == Y) and (x + y + z == N):
                print("x", x, "y:", y, "z:", z)
                flg = 1
                break
            # print("x", x, "y:", y, "z:", z)
            x += 1
        if flg == 1:
            break
        y += 1
    if flg == 1:
        break
    z += 1
else:
    print(-1, -1, -1)

# if Y >= 10:
#     while Y >= 10:
#         Y -= 10
#         x += 1
# print("Y:", Y, "x:", x)
# if Y >= 5:
#     while Y >= 5:
#         Y -= 5
#         y += 1
# print("Y:", Y, "y:", y)
# while Y >= 1:
#     Y -= 1
#     z += 1

# if (x + y + z == N):
#     print("10000円札x:", x, "枚\n", "5000円札y:", y, "枚\n",
#      "1000円札z:", z, "枚")

# while (x * 10 + y * 5 + z <= Y) and (flg == 0):
#
#     while (x * 10 + y * 5 + z <= Y) and (flg == 0):
#
#         while (x * 10 + y * 5 + z <= Y) and (flg == 0):
#             if ((x * 10) + (y * 5) + (z)) == Y:
#                 flg = 1
#                 break
#                 x += 1
#         y += 1
#     z += 1


print()
# In[]:

# In[]:

# In[]:

# In[]:

# In[]:

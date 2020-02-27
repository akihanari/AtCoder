# %% [markdown]
# **ABC049C - 白昼夢**<br>

# In[]:
# erasedream  # 結果：WA
import re
S = input()
U = ['dream', 'dreamer', 'erase', 'eraser']

# print("S:", S)
# print("len:", len(S))
S = S[::-1]
# print("S:", S)
U = [i[::-1] for i in U]
# print("U:", U)

j = 0
flg = 0
while flg < 2:
    j = 0
    while j < 4:
        if S.startswith(U[j]):
            # print("U[j]:", U[j])
            S = re.sub(U[j], '', S)
            # print("S::", S)
        j += 1
    flg += 1
# print(S)
if len(S) > 0:
    print('NO')
else:
    print('YES')

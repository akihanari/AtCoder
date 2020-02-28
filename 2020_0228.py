# %% [markdown]
# **ABC049C - 白昼夢**<br>

# In[]:
# erasedream  # 結果：WA
import re
S = input()

S = S[::-1]
# print("S::", S)

n_len = len(S)
# print("n_len:", n_len)
flg = True
count = 0
while count < n_len:
    m = re.search('maerd|remaerd|esare|resare', S[count:])
    # print("m.start():", m.start(), "count:", count)
    if m and m.start() == 0:
        count += m.end()
        # print("S::", S[count:], "count:", count)
    else:
        flg = False
        # print("False")
        break
if flg:
    print('YES')
else:
    print('NO')
print()

# In[]:

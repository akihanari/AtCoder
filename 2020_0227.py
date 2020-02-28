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
print("S:", S)
U = [i[::-1] for i in U]
print("U:", U)

j = 0
flg = 0
while flg != len(S):
    j = 0
    flg = len(S)
    while j < 4:
        if S.startswith(U[j]):
            # print("U[j]:", U[j])
            S = re.sub(U[j], '', S)
            # print("S::", S)
        j += 1
    # flg = len(S)
if len(S) == 0:
    print('YES')
else:
    print('NO')

# In[]:
# erasedream  # 結果：WA
import re
S = input()
# U = ['dream', 'dreamer', 'erase', 'eraser']

print("S:", S)
print("len:", len(S))
S = S[::-1]
print("S::", S)
# U = [i[::-1] for i in U]
# print("U:", U)

j = 0
n_len = len(S)
flg = True
count = 0
while count < n_len:
    m = re.search('maerd|remaerd|esare|resare', S[count:])
    print("m.start():", m.start(), "count:", count)
    if m and m.start() == count:
        count += m.end()
        # print("S::", S[count:], "count:", count)
    else:
        flg = False
        break
    j += 1
if flg:
    print('YES')
else:
    print('NO')
print()

# In[]:
S: remaerdmaerd
U: ['maerd', 'remaerd', 'esare', 'resare']

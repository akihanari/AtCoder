# %% [markdown]
# **ABC049C - 白昼夢**<br>


# In[]:
# erasedream
import re
S = input()
U1 = ['dream', 'erase']
U2 = ['dreamer', 'eraser']

print("S:", S)
print("len:", len(S))
S = S[::-1]
print("S:", S)
U1 = [i[::-1] for i in U1]
print("U1:", U1)
U2 = [i[::-1] for i in U2]
print("U2:", U2)


i = 0
j = 0
while i < len(S) and j < 2:
    if U1[j] in S:
        if U2[j] in S:
            S = re.sub(U2[j], '', S)
        else:
            S = re.sub(U1[j], '', S)
        print("S::", S)
    j += 1
if len(S) > 0:
    print('NO')
else:
    print('YES')


# In[]:
# erasedream  # あともう一息
import re
S = input()
U = ['dream', 'dreamer', 'erase', 'eraser']

print("S:", S)
print("len:", len(S))
S = S[::-1]
print("S:", S)
U = [i[::-1] for i in U]
print("U:", U)

j = 0
while j < 4:
    if S.startswith(U[j]):
        print("U[j]:", U[j])
        S = re.sub(U[j], '', S)
        print("S::", S)
    j += 1
print(S)
if len(S) > 0:
    print('NO')
else:
    print('YES')

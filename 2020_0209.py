# %% [markdown]
# **PracticeA**
# 文字列Sの書かれたボールがA個、文字列Tの書かれたボールがB個あります。
# 高橋君は、文字列Uの書かれたボールを１個選んで捨てました。
# 文字列S,Tの書かれたボールがそれぞれ何個残っているでしょうか。
# ・S,T,Uは英小文字のみからなる文字列
# ・S,Tの長さは1以上10以下
# ・SはTではない
# ・S=UまたはT=U
# ・1<=A,B<=10
# ・A,Bは整数

# In[]:
# -*- coding: utf-8 -*-
# スペース区切りの文字列の入力
a, b = map(str, input().split())
print("a:", a, "b:", b)
# スペース区切りの整数の入力
c, d = map(int, input().split())
print("c:", c, "d", d)
# 文字列の入力
e = input()
print("e", e)
if a == e:
	print(c - 1, d)
else:
	print(c, d - 1)
# In[]:

# %% [markdown]
# **PracticeB**
# 文字列Sが与えられます。Sのすべての文字列を'x'で置き換えて出力してください。
# ・Sは英小文字のみからなる文字列
# ・Sの長さは1以上100以下

# In[]:
# -*- coding: utf-8 -*-
# 案2
import re
a = input()
print(re.sub('[a-z]', 'x', a))

# In[]:

# %% [markdown]
# **PracticeC**
# 整数列A1,A2,...,Anが与えられます。
# この整数列のどの2つの要素も互いに異なるならば'YES'を、
# そうでないなら'NO'を出力してください。
# ・2<=N<=200000
# ・1<=Ai<=10の9乗
# ・入力はすべて整数

# In[]:
# -*- coding: utf-8 -*-
a = int(input())
print("a:", a)
#b = set()
#for i in range(a):
#	b ^= {input()}
b = input().split()
print("b:", b)
if len(set(b)) != len(b):
	print('NO')
else:
	print('YES')

# In[]:

# %% [markdown]
# **PracticeD**
# N個のサイコロが左から右に一列に並べてあります。
# 左からi番目のサイコロは1からpiまでのpi種類の目がそれぞれ等確率で出ます。
# 隣接するK個のサイコロを選んでそれぞれ独立に振ったとき、
# 出る目の合計の期待値の最大値を求めてください。
# ・1<=K<=N<=200000
# ・1<=Ai<=1000
# ・入力で与えられる値はすべて整数

# In[]:
# -*- coding: utf-8 -*-
a, b = map(int, input().split())
#print("a:", a, "b:", b)
c = input().split()
print("c:", c)
#print(type(c))
#print("c:", c)
d = []
for i in range(a - b + 1):
#	print(int(c[i]))
	h = 0
	for j in range(b):
		h += int(c[i + j])
		print(h)
	d.append(h)
	print("d", d)
print("max",d.index(max(d)))
e = 0
g = d.index(max(d))
for i in range(b):
	f = int(c[i + g])
#	print("f:", f)
	d = 0
	for j in range(f):
		d += (j + 1)
#		print("d:", d)
	e += d / f
#	print("e:", e)
print("!e:", e)
#print(((1 + 2) / 2)+((1 + 2 + 3 + 4) / 4)+((1 + 2 + 3 + 4 + 5)/ 5))

# In[]:
# 他参加者回答例
n, k = map(int,input().split())
print("n:", n, "k:", k)
P = list(map(int,input().split()))
print("P:", P)
ave=[(p+1)/2 for p in P]
print("ave:", ave) #
s=sum(ave[:k])
ans=s
for left in range(n-k):
    s -= ave[left]
    s += ave[left+k]
    if s>ans:
        ans = s
print(ans)

# In[]:
# input().splitの書き方の違い
# -*- coding: utf-8 -*-
a, b = map(int, input().split())
print("a:", a, "b:", b)
c = list(map(int, input().split()))
d = map(int, input().split())
e = input().split()
print("c:", c)
print("d:", d)
print("e:", e)
print("type a:", type(a))
print("type b:",type(b))
print("type c:",type(c))
print("type c[0]:",type(c[0]))
print("type d:",type(d))
#print("type d[0]:",type(d[0]))
print("type e:",type(e))
print("type e[0]:",type(e[0]))

# In[]:
# 再チャレンジ(結果：TLE)
# -*- coding: utf-8 -*-
a, b = map(int, input().split())
print("a:", a, "b:", b)
c = list(map(int, input().split()))
print("c:", c)
#print("type a:", type(a))
#print("type b:",type(b))
#print("type c:",type(c))
#print("type c[0]:",type(c[0]))

#print("c:", c)
d = []
for i in range(a - b + 1):
#	print(c[i])
	h = 0
	for j in range(b):
		h += c[i + j]
#		print(h)
	d.append(h)
#	print("d", d)
print("max",d.index(max(d)))
e = 0
g = d.index(max(d))
for i in range(b):
	f = c[i + g]

#	print("f:", f)
	d = 0
	for j in range(f):
		d += (j + 1)
#		print("d:", d)
	e += d / f
#	print("e:", e)
print("!e:", e)

# In[]:
# 再再チャレンジ(結果：TLE)
# -*- coding: utf-8 -*-
a, b = map(int, input().split())
print("a:", a, "b:", b)
c = list(map(int, input().split()))
print("c:", c)
d = []
#h = 0
for i in range(a - b + 1):
	h = sum(c[i:b + i])
	d.append(h)
	print("h:", h, "i:", i)
e = 0
#f = 0
g = d.index(max(d))
print("max", d.index(max(d)))
for i in range(b):
	f = sum(range(1, c[g + i] + 1))
	e += f / c[g + i]
print("!e:", e)

# In[]:
# 再再再チャレンジ(結果：TLE)
# -*- coding: utf-8 -*-
a, b = map(int, input().split())
print("a:", a, "b:", b)
c = list(map(int, input().split()))
print("c:", c)
d = [su"m(c[i:b + i]) for i in range(a - b + 1)]
print("d", d)
e = 0
g = d.index(max(d))
print("max", d.index(max(d)))
for i in range(b):
	e += sum(range(1, c[g + i] + 1)) / c[g + i]
#	print("e", sum(range(1, c[g + i] + 1)) / c[g + i])
print("!e:", e)
# In[]:
# 再再再再チャレンジ(結果：TLE)
# -*- coding: utf-8 -*-
a, b = map(int, input().split())
print("a:", a, "b:", b)
c = list(map(int, input().split()))
print("c:", c)
d = [(sum(range(1, c[i] + 1)) / c[i]) for i in range(a)]
print("d:", d)
e = [sum(d[i:b + i]) for i in range(a - b + 1)]
print("e", e)
g = max(e)
print("g:", g)
#	print("e", sum(range(1, c[g + i] + 1)) / c[g + i])
#print("!e:", e)

# In[]:
# 再再再再再チャレンジ(結果：TLE)
# -*- coding: utf-8 -*-
a, b = map(int, input().split())
print("a:", a, "b:", b)
c = list(map(int, input().split()))
print("c:", c)
d = [(i + 1) / 2 for i in c]
print("d:", d)
e = [sum(d[i:b + i]) for i in range(a - b + 1)]
print("e", e)
print(max(e))

# In[]:
# 再再再再再再チャレンジ(結果：TLE)
# -*- coding: utf-8 -*-
a, b = map(int, input().split())
print("a:", a, "b:", b)
c = list(map(int, input().split()))
print("c:", c)
d = [(i + 1) / 2 for i in c]
print("d:", d)
e = sum(d[:b])
print("e", e)
for i in range(a - b + 1):
	f = sum(d[i:b + i])
	if f > e:
		e = f
print(e)

# In[]:
# 再再再再再再チャレンジ(結果：AC)
# -*- coding: utf-8 -*-
a, b = map(int, input().split())
print("a:", a, "b:", b)
c = list(map(int, input().split()))
print("c:", c)
d = [(i + 1) / 2 for i in c]
print("d:", d)
e = sum(d[:b])
print("e", e)
f = e
for i in range(a - b):
	f -= d[i]
	f += d[i + b]
	print("f", f)
	if f > e:
		e = f
print(e)

# In[]:

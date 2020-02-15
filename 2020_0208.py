# print("Hello World!")

# In[]:

# %% [markdown]
# **PracticeA - Welcome to AtCoder**
# 高橋君はデータの加工が行いたいです。
# 整数 a,b,cと、文字列 s が与えられます。 a+b+c の計算結果と、文字列 s を並べて表示しなさい。

# In[]:
# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())
# 文字列の入力
s = input()
# 出力
print("{} {}".format(a+b+c, s))

# In[]:
# -*- coding: utf-8 -*-
# 案1
a = int(input())
numlist = []
for i in range(a):
	b = int(input())
	if b in numlist:
		numlist.remove(b)
	else:
		numlist.append(b)
print(len(numlist))

# In[]:
# -*- coding: utf-8 -*-
# 案2
a = int(input())
numlist = []
for i in range(a):
	b = int(input())
	numlist.append(b)
i = 0
while i < a - 1:
    j = i + 1
    while j < a:
        if (numlist[i] == numlist[j]):
            numlist.pop(i)
            numlist.pop(j - 1)
            a -= 2
        j += 1
    i += 1
print(len(numlist))

# In[]:
# -*- coding: utf-8 -*-
# 案3
a = int(input())
numlist = []
for i in range(a):
	b = int(input())
	numlist.append(b)
print(numlist)
numlist.sort()
print(numlist)
i = 0
flg == 0
while(i < a - 1):
	j = i + 1
	while(j < a):
		if numlist[i] == numlist[j]:
			numlist.pop(i)
			numlist.pop(j - 1)
			a -= 2
			flg == 1
			print(numlist)
		j += 1
	if flg == 0
		i += 1
print(len(numlist))

# In[]:
# -*- coding: utf-8 -*-
# 案4
a = int(input())
#numlist = []
b = set()
for i in range(a):
	b ^= {input()}
	print(b)
#	if b in numlist:
#		numlist.remove(b)
#	else:
#		numlist.append(b)
print("len", len(b))

# In[]:
a, b = map(int, input().split())
#print(float(abs((b % 12) - (c % 12))))
#print(23 % 12)
#print(59 % 12)
#print(360 / 12)
c = (a % 12) * (360 / 12)
if a == 0:
	c = 0
print("c", c)
d = ((360 / 12) / 60) * b
if b == 0:
	d = 0
print("d", d)
e = b * (360 / 60)
if b == 0:
	e = 0
print("e", e)
f = c + d - e
print("f", f)


# In[]:
a, b = map(int, input().split())
c = (a % 12) * 30
if a == 0:
	c = 0
d = b / 2
e = b * 6
print("e", e)
if b == 0:
	d = 0
	e = 0
f = abs((c + d) - e)
#if type(f) == int:
print(min(f, 360 -f))
#else:
#	print('{:.4f}'.format(f))

# In[]:

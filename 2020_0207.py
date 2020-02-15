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

# In[]:

# In[]:

# In[]:

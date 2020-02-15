
# In[]:

# %% [markdown]
# **ABC086A - Product**
# シカのAtCooDeerくんは二つの正整数a,bを見つけました。
# aとbの積が偶数か奇数か判定してください。
# 積が奇数なら'Odd'と、偶数なら'Even'と出力せよ。

# In[]:
# -*- coding: utf-8 -*-
a, b = map(int, input().split())
print("a:", a, "b:", b)
if (a % 2 == 0) or (b % 2 == 0):
	print('Even')
else:
	print('Odd')
# In[]:

# %% [markdown]
# **ABC081A - Placing Marbles**
# すぬけ君は1,2,3の番号がついた3つのマスからなるマス目を持っています。
# 各マスには'0'か'1'が書かれており、マスiにはsiが書かれています。
# すぬけ君は'1'が書かれたマスにビー玉を置きます。
# ビー玉が置かれるマスがいくつあるか求めてください
# ・s1,s2,s3は'1'あるいは'0'

# In[]:
# -*- coding: utf-8 -*-
s = list(map(int,input()))
print("s[0]:", s[0], "s[1]:", s[1], "s[2]", s[2])
count = 0
for i in range(3):
	print(i, s[i])
	if s[i] == 1:
		count += 1
print(count)

# In[]:

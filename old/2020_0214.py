# %% [markdown]
# **ABC083B - Some Sums**
# 1以上N以下の整数のうち、10進法での各桁の和がA以上B以下であるものの
# 総和を求めてください。
# ・1 <= N <= 10^4
# ・1 <= A <= B <= 36
# ・入力はすべて整数である

# In[]:
# -*- coding: utf-8 -*-
n, a, b = list(map(int, input().split()))
print("n:", n, "a:", a, "b:", b)
#nums = [i for i in range(1, n + 1)]
#print(nums)
sumlist = 0
for num in range(1, n+1):
	#print("num:", num)
	snum = 0
	if num > 9:
		tmp = num
		#print("tmp:", tmp)
		while tmp > 0:
			snum += tmp % 10
			tmp = int(tmp / 10)
		#print("snum:", snum)
		if a <= snum <= b:
			#print("num:", num)
			sumlist += num
	elif a <= num <= b:
		#print("num:", num)
		sumlist += num
print("sumlist", sumlist)


# In[]:

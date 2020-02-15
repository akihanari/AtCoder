# %% [markdown]
# **ABC081B - Shift only**
# 黒板にN個の正の整数A1,...,ANが書かれています。
# すぬけ君は、黒板に書かれている整数がすべて偶数であるとき、
# 次の操作を行うことができます。
# ・黒板に書かれている整数すべてを、2で割ったものに置き換える
# すぬけ君は最大で何回操作を行うことができるかを求めてください。
# 1 <= N <= 200
# 1 <= Ai <= 10^9

# In[]:
# -*- coding: utf-8 -*-
a = int(input())
print("a:", a)
b = list(map(int, input().split()))
print("b:", b)
count = 0
flg = True
while True:
	for i in range(a):
		if b[i] % 2 != 0:
			flg = False
			print("i:", i)
			break
		else:
			b[i] = int(b[i] / 2)
	print("b::", b)
	if flg == False:
		break
	count += 1
print(count)

# In[]:
# %% [markdown]
# **ABC087B - Coins**
# あなたは、500円玉をA枚、100円玉をB枚、50円玉をC枚持っています。
# これらの硬貨の中から何枚かを選び、合計金額をちょうどX円にする方法は何通りありますか。
# 同じ種類の硬貨どうしは区別できません。2通りの硬貨の選び方は、
# ある種類の硬貨について、その硬貨を選ぶ枚数が異なるとき区別されます。
# ・0 <= A,B,C <= 50
# ・A + B + C >= 1
# ・50 <= X <= 20,000
# ・A,B,Cは整数である
# ・Xは50の倍数である

# In[]:
# -*- coding: utf-8 -*-ß
a = int(input()) #500
b = int(input()) #100
c = int(input()) #50
x = int(input()) #合計
count = 0
print("input: a:", a, "b:", b, "c:", c, "x:", x)
for i in range(a + 1):
	for j in range(b + 1):
		for k in range(c + 1):
			#print("i:", i, "j:", j, "k:", k, "sum:", (a * i) + (b * j) + (c * k))
			if ((500 * i) + (100 * j) + (50 * k)) == x:
				print("a:", 500 * i, "(", i, ")", "b:", 100 * j, "(", j, ")", "c:", 50 * k, "(", k, ")")
				count += 1
print("count", count)

# In[]:

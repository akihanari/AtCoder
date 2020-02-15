# %% [markdown]
# **ABC088B - Card Game for Two**
# N枚のカードがあrます。i枚目のカードにはaiという数が書かれています。
# AliceとBobは、これらのカードを使ってゲームを行います。
# ゲームでは、AliceとBobが交互に1枚ずつカードを取っていきます。
# Aliceが先にカードを取ります。
# 2人がすべてのカードを取った時にゲームは終了し、取ったカードの数の合計が
# その人の合計になります。2人とも自分の得点を最大化するように最適な戦略を取った時、
# AliceはBobより何点多く取るかを求めてください。
# ・Nは1以上100以下の整数
# ・ai(1 <= i <= N)は1以上100以下の整数

# In[]:
# -*- coding: utf-8 -*-
N = int(input())
print("N:", N)
a = list(map(int, input().split()))
print("a:", a)
a.sort(reverse = True)
sum_a = sum(a[::2])
print("sum_a", sum_a)
a.insert(0, 0)
sum_b = sum(a[::2])
print("sum_b", sum_b)
print(sum_a - sum_b)

# In[]:

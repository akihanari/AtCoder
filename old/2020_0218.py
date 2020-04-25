# %% [markdown]
# **ABC 155 D - Pairs**<br>
# N個の整数A1,A2,...,ANがあります。<br>
# このうち2つを選んでペアにする方法はN(N-1)/2通りありますが、<br>
# それぞれのペアについて積を求め、小さい順に並べ替えたとき、<br>
# K番目にくる数は何になるでしょうか？<br>
# ・入力はすべて整数<br>
# ・2 <= N <= 2 × 10^5<br>
# ・1 <= K <= N(N-1)/2<br>
# ・-10^9 <= Ai <= 10^9(1 <= i <= N)<br>

# In[]:  # ダメだったやつ
import itertools
N, K = map(int, input().split())
print("N:", N, "K:", K)
A = list(map(int, input().split()))
print("A:", A)
A.sort()
print("sortA:", A)
lst = [i[0]*i[1] for i in itertools.combinations(A, 2)]
print("lst:", lst)
lst.sort()
print("sortlst:", lst)
print("answer:", lst[K - 1])
print()

# In[]:  # 今日書いたやつ
import numpy as np

# # 一次元配列
# test_arr = np.asarray([1, 2, 3])
# print("test_arr")
"""
4 3
3 3 -4 -2
"""
N, K = map(int, input().split())
print("N:", N, "K:", K)
A = list(map(int, input().split()))
print("A:", A)
A = np.array(A)
print("A:", A)
A.sort()
print("sortA:", A)
print()

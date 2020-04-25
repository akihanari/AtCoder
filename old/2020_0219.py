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
lst = [i[0]*i[1] for i in itertools.combinations(A,2)]
print("lst:", lst)
lst.sort()
print("sortlst:", lst)
print("answer:", lst[K - 1])
print()

# In[]:  # 今日書いたやつ
import numpy as np
# numpyを使う
"""
4 3
3 3 -4 -2
"""
N, K = map(int, input().split())
print("N:", N, "K:", K)
A = np.array([int(i) for i in input().split()])
print("A:", A)
print(type(A))
A.sort()
print("sortA:", A)

A_max = max(np.abs(A))
print("A_max:", A_max)
A_minus = A[A<0]
print("A_minus:", A_minus)
A_zero = A[A==0]
print("A_zero:", A_zero)
A_plus = A[A>0]
print("A_plus:", A_plus)

def check(x):
    ret = 0
    if x >= 0:
        ret += N * len(A_zero)
    ret += np.searchsorted(A, x // A_plus, side='right').sum()
    ret += (N - np.searchsorted(A, -(x // -A_minus))).sum()
    ret -= np.count_nonzero(A * A <= x)
    print("ret:", ret)
    return ret // 2

right = A_max * A_max
left = -right - 1
while (right - left > 1):
    middle = (right + left) >> 1
    if check(middle) < K:
        left = middle
    else:
        right = middle
print(right)

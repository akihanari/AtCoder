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

# 一次元配列
test_arr = np.asarray([1, 2, 3])
print("test_arr")

# %% [markdown]
# **他の人の回答1**<br>
# In[]:
import numpy as np

n,k=map(int,input().split())
A=np.array(input().split(),np.int64)
A.sort()

zero=A[A==0]
neg=A[A<0]
pos=A[A>0]

def f(x): # count pairs x or less
    cnt=0
    #zero
    if x>=0:
        cnt += len(zero)*n
    #pos
    cnt += A.searchsorted(x//pos,side="right").sum()
    #neg
    cnt += (n-A.searchsorted(-(-x//neg),side="left")).sum()
    #except a*a
    cnt-=np.count_nonzero(A*A<=x)
    return cnt//2

l=-10**18
r=10**18

while l<r:
    pov=(l+r)//2
    if f(pov)>=k:
        r=pov
    else:
        l=pov+1
print(l)

# %% [markdown]
# **他の人の回答2**<br>

# In[]:
# これは500点では？
import numpy as np

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = np.array(a) # numpy の array で高速化
a.sort()

zero = np.count_nonzero(a == 0)
positive = a[a > 0] # numpy の特徴的な記法
negative = a[a < 0]

def count(x): # 積が x 以下のペアは何個あるか？
  ans = 0
  if x >= 0: # 片側が 0 の場合
    ans += n * zero
  ans += np.searchsorted(a, x // positive, side="right").sum() # 片側が正の場合
  ans += n * len(negative) - np.searchsorted(a, -(-x // negative), side="left").sum() # 片側が負の場合 切り上げは -(-a//b)
  ans -= np.count_nonzero(a * a <= x) # 同じもの2つは選べない
  return ans // 2

ok = 10**18
ng = -ok - 1
while ok - ng > 1: # 二分探索
  cen = (ok + ng) // 2
  if count(cen) >= k:
    ok = cen
  else:
    ng = cen
print(ok)

# In[]:

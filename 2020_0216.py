# %% [markdown]
# **ABC 155 A-Poor**<br>
# 3つ組の数について、ある2つが等しく、残りの1つがそれらと異なるとき、<br>
# その3つ組を「かわいそう」であるといいます。<br>
# 3つの整数A,B,Cが与えられるので、この3つ組がかわいそうであれば'Yes'を、<br>
# そうでなければ'No'を出力してください。<br>
# ・A,B,Cはいずれも1以上9以下の整数<br>

# In[]:
# -*- coding: utf-8 -*-
A, B, C = map(int, input().split())
#print("A:", A, "B:", B, "C:", C)
D = set([A, B, C])
#print(D)
set_len = len(D)
if set_len == 3 or set_len == 1:
    print('No')
else:
    print('Yes')

# %% [markdown]
# **ABC 155 B - Papers, Please**<br>
# あなたはAtCoder王国の入国審査官です。<br>
# 入国者の書類にはいくつかの整数が書かれており、<br>
# あなたの仕事はこれらが条件を満たすか判定することです。<br>
# 規約では、次の条件を満たすとき、またその時に限り、入国を承認することになっています。<br>
# ・書類に書かれている整数のうち、偶数であるものは全て、3または5で割り切れる。<br>
# 上の規約に従う時、書類にN個の整数A1,A2,...,ANが書かれた入国者を<br>
# 承認するならば'APPROVED'を、しないならば'DENIED'を出力してください。<br>

# In[]:
# -*- coding: utf-8 -*-
N = int(input())
#print("N:", N)
A = list(map(int, input().split()))
#print("A:", A)
for i in A:
    if i % 2 == 0:
        if not((i % 3 == 0) or (i % 5 == 0)):
            print('DENIED')
            break
else:print('APPROVED')

# %% [markdown]
# **ABC 155 C - Poll**<br>
# N枚の投票用紙があり、i(1 <= i <= N)枚目には文字列Siが書かれています。<br>
# 書かれた回数が最も多い文字列を全て、辞書順で小さい順に出力してください。<br>
# ・1 <= N <= 2 × 10^5<br>
# ・Siは英小文字のみからなる文字列(1 <= i <= N)<br>
# ・Siの長さは1以上10以下(1 <= i <= N)<br>

# In[]:
# -*- coding: utf-8 -*-
import collections
N = int(input())
#print("N:", N)
S = [input() for i in range(N)]
#print("S:", S)
c = collections.Counter(S)
values, counts = zip(*c.most_common())
#print("values:", values)
#print("counts:", counts)
i = 0
lst = [values[i] for i in range(len(c)) if counts[0] == counts[i]]
#print("lst:", lst)
lst.sort()
for i in lst:
    print(i)

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

# In[]:
# 提出1(結果:TLE)
# -*- coding: utf-8 -*-
import itertools
N, K = map(int, input().split())
A = list(map(int, input().split()))
lst = [i[0]*i[1] for i in itertools.combinations(A,2)]
lst.sort()
print(lst[K - 1])


# In[]:
# 提出2(結果:TLE)
import itertools
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
lst = [i[0]*i[1] for i in itertools.combinations(A,2)]
lst.sort()
print(lst[K - 1])

# In[]:

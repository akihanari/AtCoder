# %% [markdown]
# **ABC085C - Otoshidama**<br>

# In[]:
# 提出結果:WA
# N枚のお札の合計金額がY円となることがありえるか
def num_judge(n, Y, N):
    if int(Y / n) > N:
        max = N
    else:
        max = int(Y / n)
    return max

N, Y = map(int, input().split())

Y = int(Y / 1000)

x_max = num_judge(10, Y, N)
y_max = num_judge(5, Y, N)

x = 0
flg = 0

while x <= x_max:
    y = 0
    while y <= y_max:
        z = N - (x + y)
        if (z >= 0) and (x * 10 + y * 5 + z == Y):
            print(x, y, z)
            flg = 1
            break
        y += 1
    if flg == 1:
        break
    x += 1
else:
    print(-1, -1, -1)
# %% [markdown]
# **ABC156**<br>

# %% [markdown]
# **A - Beginner**<br>
# In[]:
N, R = map(int, input().split())
print("N:", N, "R:", R)
if N <= 10:
    R = R + (100 * (10 - N))
print(R)
print()

# %% [markdown]
# **B - Digits**<br>

# In[]:
N, K = map(int, input().split())
print("N:", N, "K:", K)
n = 1
# print(pow(K, n))

while True:
    if pow(K, n) <= N < pow(K, n + 1):
       break
    n += 1
print(n + 1)

# %% [markdown]
# **C - Rally**<br>
# In[]:
N = int(input())
# print("N:", N)
X = list(map(int, input().split()))
# print("X:", X)
B = []
for j in range(1, 101):
    #print(":", (X[0] - 2)**2)
    A = [(i - j)**2 for i in X]
    # print("j:", j, "A:", A)
    B.append(sum(A))
# print("B:", B)
print(min(B))

# %% [markdown]
# **D - Bouquet**<br>
# In[]:
import math

def count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n, a, b = map(int, input().split())
c_lst = [i for i in range(1, n + 1) if (i != a) and (i != b) ]
print("n:", n, "a:", a, "b:", b)
print("c_list:", c_lst)
lst_s = []
for i in c_lst:
    lst_s.append(count(n,i))

lst_s = sum(lst_s) % (10**9 + 7)
print("sum:", lst_s)


# In[]:
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

n, a, b = map(int, input().split())
c_lst = [i for i in range(1, n + 1) if (i != a) and (i != b) ]
print("n:", n, "a:", a, "b:", b)
print("c_list:", c_lst)
#lst_s = []
#for i in c_lst:
#    lst_s.append(count(n,i))

#lst_s = sum(lst_s) % mod
#print("sum:", lst_s)

mod = 10**9+7 #出力の制限
# N = 10**4
#g1 = [1, 1] # 元テーブル
#g2 = [1, 1] #逆元テーブル
lst_r = list(c_lst.reverse())
lst_ = [i for i in range(len(c_lst)]] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    c_lst.append( ( c_lst[-1] * i ) % mod )
    lst_.append( ( -lst_[mod % i] * (mod//i) ) % mod )
    lst_r.append( (lst_r[-1] * lst_[-1]) % mod )

a = cmb(n,r,mod)
print(a)


# In[]:

# In[]:

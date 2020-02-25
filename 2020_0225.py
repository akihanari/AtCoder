# %% [markdown]
# **ABC156 D - Bouquet**<br>
# あかりさんはn種類の花を1本ずつ持っていました。<br>
# あかりさんは、これらの花から1本以上を選び、花束を作ろうとしています。<br>
# ただし、あかりさんはaとbの2つの数を苦手としていて、いずれかと一致<br>
# するような本数の花からなる花束は作ることができません。<br>
# あかりさんがつくることのできる花束は何種類あるでしょうか。<br>
# (10^9 + 7)で割った余りを求めてください。<br>
# ここで2つの花束は、一方では使われているが、もう一方では使われていない<br>
# 種類の花があるとき、別の種類の花束であるとみなします、<br>
# ・入力はすべて整数である
# 2 <= n <= 10^9
# 1 <= a < b <= min(n,2 × 10^5)
# In[]:
n, a, b = map(int, input().split())
print("n:", n, "a:", a, "b:", b)

# In[]:
# 他の人の解答


def cmb_mod(n, r, mod):
    x, y = 1, 1
    for i in range(r):
        x = (x * (n - i)) % mod
        y = (y * (i + 1)) % mod
    return (x * pow(y, mod - 2, mod)) % mod


n, a, b = map(int, input().split())

mod = 10**9 + 7
all_case = pow(2, n, mod) - 1

print((all_case - cmb_mod(n, a, mod) - cmb_mod(n, b, mod)) % mod)


# In[]:
# ほかの人の解答
n, a, b = map(int, input().split())
mod = 10**9+7


def nCk(n, k):
    x = 1
    y = 1
    for i in range(k):
        x = (x*(n-i)) % mod
        y = (y*(k-i)) % mod
    y_inv = pow(y, mod-2, mod)
    return (x*y_inv) % mod


ans = (pow(2, n, mod) - 1 - nCk(n, a) - nCk(n, b)) % mod
print(ans)

# In[]:
# 他の人の解答
n, a, b = map(int, input().split())

p = 10 ** 9 + 7
inv = [0] * (b + 1)
inv[1] = 1

for k in range(2, b + 1):
    inv[k] = pow(k, p - 2, p)

com = 1
for i in range(1, a + 1):
    com = (com * (n + 1 - i)) % p * inv[i]

coma = com

for j in range(a + 1, b + 1):
    com = (com * (n + 1 - j)) % p * inv[j]

comb = com

print((pow(2, n, p) - 1 - coma - comb) % p)

# In[]:
# 他の人の解答
import functools
n, a, b = map(int, input().split())
mod = 10**9+7

def f(n: int, a: int) -> int:
    n = functools.reduce(lambda x, y: x*y%mod, range(n, n-a, -1))
    d = functools.reduce(lambda x, y: x*y%mod, range(1, a+1))
    return n*pow(d, mod - 2, mod)%mod

ans = pow(2,n,mod) - f(n, a) - f(n, b) - 1
ans %= mod
print(ans)


# In[]:

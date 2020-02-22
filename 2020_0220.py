# %% [markdown]
# **ABC085B - Kagami Mochi**<br>

# In[]:
import numpy as np
N = int(input())
# print("N:", N)
d = np.array([int(input()) for i in range(N)])
# print("d:", d)

d_uni = np.unique(d)
# print("d_uni:", d_uni)

print(len(d_uni))

# In[]:

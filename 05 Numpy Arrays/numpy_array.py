# %% [markdown]
"""
# Numpy Array
Use of numpy arrays is to do calculations on large data
"""
# %%
# Converting a list into array
a = [12, 13, 11, 15, 14]
print(a, type(a))
# %%
import numpy as np
a1 = np.array(a)
print(a1, type(a1))
# %%
# ndarray means n-dimensional array
a1.ndim
# %%
a1.shape
# %%
a1.size
# %%
a1.dtype
# %% [markdown]
"""
# Creating a 2D array
"""
# %%
b = [
    [11, 12, 13, 14],
    [15, 16, 17, 18]
]
print(b, type(b))
# %%
b1 = np.array(b)
print(b1, type(b1))
# %%
b1.ndim
# %%
b1.shape
# %%
b1.size
# %%
b1.dtype
# %% [markdown]
"""
Creating a 3d array
"""
c = [
    [[15, 16, 17, 18],
     [19, 20, 21, 22],
     [23, 24, 25, 26]],

    [[27, 28, 29, 30],
     [31, 32, 33, 34],
     [35, 36, 37, 38]]
]
print(c, type(c))
# %%
c1 = np.array(c)
print(c1, type(c1))
# %%
c1.ndim
# %%
c1.shape
# %%
c1.size
# %%
c1.dtype
# %%
d = [12.3, 11.1, 14.2, 15.1]
d1 = np.array(d)
d1.dtype
# %% [markdown]
"""
# Multiplying any number to list vs numpy array
"""
# %%
# Multiplying 3 in a list
# You need to use for loop on list to apply mathematical operations
e = [12, 13, 14, 15, 16]
f = []

for i in e:
    f.append(i*3)

print(e, f)
# %%
g = np.array(e)
h = 3 * g
print(g, h)
# %%
i = list(range(1, 1000))
print(i)
len(i)
# %%
k = []
for a in i:
    k.append(a**2)
print(k)
# %%
i1 = np.array(i)
j = i1 ** 2
print(j)
# %%
k = np.sqrt(i1)
print(k)
# %% [markdown]
"""
## Calculations in numpy array are faster than list for larget data
"""

# %% [markdown]
"""
# Aggregation operations
1. sum
2. mean
3. max
4. min
5. std
"""
# %%
a = [
    [2, 3, 4, 5],
    [6, 7, 8, 9],
    [10, 11, 12, 13]
]
print(a)
# %%
a1 = np.array(a)
print(a1)
# %%
a1.sum()
# %%
a1.mean()
# %%
a1.max()
# %%
a1.min()
# %%
a1.std()
# %%
a1.sum(axis=0)
# %%
a1.sum(axis=1)
# %%
a1.mean(axis=0)
# %%
a1.mean(axis=1)
# %%
# Range function can generate only integers
a = np.arange(start=0, stop=10, step=0.5)
print(a)
# %%
b = np.linspace(start=0.1, stop=10, num=10)
b
# %%
b.shape
# %% [markdown]
"""
# Generating Random data in numpy
"""
# %%
# Random number between 0 to 1
np.random.random()
# %%
c = np.random.random(size=100)
print(c)
# %%
# Generate random integers
# Generating dice throws
d = np.random.randint(low=1, high=7, size=100)
print(d)
# %%
d.shape
# %%
np.unique(d)
# %%
# Normal distribution
h = np.random.normal(loc=5.5, scale=0.5/3, size=10_000)
print(h)
# %%
import seaborn as sns
sns.histplot(h, kde=True)
# %% [markdown]
"""
Mathematical operations
1. sqrt
2. exp
3. log
4. sin, asin
5. cos, acos
6. tan, atan
"""
# %%
a = [1, 2, 3, 4, 5]
np.sqrt(a)
# %%
np.exp(1)
# %%
np.exp(a)
# %%
np.log(a)
# %%
np.log10(a)
# %%
# Angle is required in radians
# 1 radian = pi/180 degrees
ang_deg = [0, 30, 45, 60, 90]
ang_rad = np.radians(ang_deg)
ang_rad
# %%
np.sin(ang_rad)
# %%
np.cos(ang_rad).round(4)
# %%
np.tan(ang_rad)
# %%
b = [0, 0.1, 0.2, 0.3, 0.5, 0.8, 0.9, 1]
# %%
np.asin(b)
# %%
np.acos(b)
# %%
np.atan(b)
# %% [markdown]

"""
# Miscillaneous functions
1. flatten / ravel
2. reshape
"""
# %%
c = [
    [2, 3, 4, 5],
    [6, 7, 8, 9],
    [10, 11, 12, 13]
]
c1 = np.array(c)
c1
# %%
d1 = c1.flatten()
print(d1)
print(d1.ndim)
# %%
d2 = c1.ravel()
print(d2.ndim)
# %%
e1 = c1.reshape(6, 2)
print(e1)
# %%
e2 = c1.reshape(4, 3)
print(e2)
# %%
print(c1)
# %%
e3 = c1.reshape(2, 6)
print(e3)
# %%
e4 = c1.reshape(1, -1)
print(e4)
# %%
e4.shape
# %%

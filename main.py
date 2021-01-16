import numpy as np
# https://morioh.com/p/75861acc02a4?f=5c21fb01c16e2556b555ab32&fbclid=IwAR3VBwA4R_hQZBvbw27i82zn-q9tNf2ZvwaMkKh8uNG5aniSamf5QMXWd4M
# nlist = [1, 2, 3, 4, 5, 6]
# nparray = np.array(nlist)
# print(nlist)
# print(nparray)
#
# L = [1, 2, 3]
# NA = np.array(L)
# for i in L:
#     print(i)
# for i in NA:
#     print(i)
#
# L1 = L + [4]
# print(L1)
# L1.append(5)
# print(L1)
#
# NA1 = NA + [4]
# print(NA1)
#
# NA2 = NA + NA
# print(NA2)
#
# L3 = []
# for i in L:
#     L3.append(i + i)
# print(L3)
#
# print(NA*2)
# print(NA**2)
# print(np.sqrt(NA))
# print(np.log(NA))
# print(np.exp(NA))

a = np.array([1, 2, 3])
b = np.array([[1, 2],
              [3, 4],
              [5, 6]])
print(a[0])  # 1
print(b[0])  # [1 2]
print(b[0][0])  # 1
print(b[0, 0])  # 1
print(b[2, 1])  # 6
print(b.T)      # [[1 3 5][2 4 6]]  transpose
print(b.shape)  # (3, 2) shape of array  3 rows, 2 columns
c = b.T         # transpose b into c
print(c.shape)  # (2, 3)
print(b.ndim)   # 2
print(a.ndim)   # 1
print(b.size)   # 6
print(a.dtype)  # int32
print(b.dtype)  # int32
d = np.array([1.1, 1.2, 1.3])
print(d.dtype)  # float64
e = np.array([1, 2], dtype=np.float64)
print(e)        # [1. 2.]
print(b.itemsize)  # 4  number of bytes
print(a.itemsize)  # 4
print(e.itemsize)  # 8
print(a.min())     # 1  lowest value
print(b.min())     # 1
print(e.min())     # 1.0
print(e.max())     # 2.0 highest value
print(b.sum())     # 21  sum all elements
print(e.sum())     # 3.0
print(b.sum(axis=0))  # [9 12]  sum of columns
print(b.sum(axis=1))  # [3 7 11]  sum of rows

f = np.zeros((2, 3))  # initialize array
print(f)          # [[0. 0. 0.] [0. 0. 0.]]
print(f.itemsize)     # 8
f = np.ones((2, 3))
print(f)          # [[1. 1. 1.] [1. 1. 1.]]
f = np.ones((3, 2), dtype=np.int16)
print(f)          # [[1 1] [1 1] [1 1]]
f = np.empty((2, 2), dtype=np.float)
print(f)   # [[6.11598403e-312 6.11598400e-312] [6.11598403e-312 6.11598403e-312]]
g = np.arange(1, 5)
print(g)   # [1 2 3 4]
g = np.arange(1, 5, .5)
print(g)   # [1.  1.5 2.  2.5 3.  3.5 4.  4.5]
h = np.linspace(1, 5, num=10)
print(h)   # linear array from 1 to 5 evenly spaced [1. ... 8 other numbers ... 5]
i = np.random.random((2, 3))
print(i)   # [[0.83304826 0.57155644 0.25289799] [0.74402872 0.69212865 0.43486987]]
j = np.zeros((2, 3))
print(j)   # [[0. 0. 0.] [0. 0. 0.]]
print(j.reshape((3, 2)))  # [[0. 0.] [0. 0.] [0. 0.]]
k = np.ones((1, 9))
print(k)   # [[1. 1. 1. 1. 1. 1. 1. 1. 1.]]
l = k.reshape((3, -1))
print(l)   # [[1. 1. 1.] [1. 1. 1.] [1. 1. 1.]]
m = np.zeros((3, 1))
print(m)   # [[0.] [0.] [0.]]




print("Finished correctly")

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
b = np.array([[1, 2], [3, 4], [5, 6]])
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
print(b.itemsize)  # 4
print(a.itemsize)  # 4
print(e.itemsize)  # 8
print(a.min())     # 1
print(b.min())     # 1
print(e.min())     # 1.0
print(e.max())     # 2.0


print("Finished correctly")

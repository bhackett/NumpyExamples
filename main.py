import numpy as np

# nlist = [1, 2, 3, 4, 5, 6]
# nparray = np.array(nlist)
# print(nlist)
# print(nparray)

L = [1, 2, 3]
NA = np.array(L)
for i in L:
    print(i)
for i in NA:
    print(i)

L1 = L + [4]
print(L1)
L1.append(5)
print(L1)

NA1 = NA + [4]
print(NA1)




print("Finished correctly")
import numpy as np

# print(np.__version__)

# a = np.array([1,2,3])

# print(a)
# print(a.shape)
# print(a.dtype)
# print(a.ndim)
# print(a.size)
# print(a.itemsize , 'bytes')

# print(a[0])

# a[0]=10

# print(a)

# b = a * np.array([2,0,2])
# print(b)

# l = [1,2,3]

a = np.array([1,2,3])

# print(l , a)

# l.append(4)
# # can not be done in numpy arrays
# a = a + [4] # broadcasting
# print(l , a)

# print(np.sqrt(a))

# dot products

l1 = np.array([1,2,3])
l2 = np.array([4,5,6])

dot = np.dot(l1,l2)
dot = l1 @ l2
print(dot)



import numpy as np
a = [1,2,3]
b = np.array(a)
b

a = np.array([1,2,3], float)
a

a = np.array([(1,2,3), (4,5,6), (7,8,9)])
a

a = np.zeros((2,3), dtype = float)
a

a = np.ones((3, 3))
a

a = np.arange(1, 5, 0.5)
a

a = np.eye(3)
a

a=np.random.random(5)
a

mu,sigma = 0, 0.1
np.random.normal(mu, sigma, 5)

a = np.array([(1,2), (3,4), (5,6)])
a[0]
a[1:]
a[: , :1]
a[1][1]

a = np.array([1,2,3])
for i in a:
    print(i)

a = np.array([(1,2,3), (4,5,6), (7,8,9)])
print("ndim:", a.ndim)
print("shape:", a.shape)
print("size", a.size)
print("dtype", a.dtype)

a = np.array([(1,2), (3,4)])
print(3 in a)
print(5 in a)

a = np.zeros([2,3,4])
a
a.reshape(24)

a = np.array([(1,2,3), (4,5,6), (7,8,9)])
a.transpose()
a.T

a = np.array([(1,2), (3,4), (5,6)])
a.flatten()

a = np.array([1,2,3])
a.shape
a = a[ :, np.newaxis]
a
a.shape

a = np.ones((2,2))
b = np.array([(-1,1),(-1,1)])
a
b

a + b
a

a - b
a*b
a/b

a = np.array([1,2,1])
a.sum()
a.prod()

a = np.array([5,3,1])
print("mean:",a.mean())
print("var:", a.var())
print("std:", a.std())
print("max:", a.max())
print("min:", a.min())

a = np.array([1.2, 3.8, 4.9])
print("argmax:", a.argmax())
print("argmin:", a.argmin())
print("ceil:", np.ceil(a))
print("floor:", np.floor(a))
print("rint:", np.rint(a))

a = np.array([16,31,12,28,22,31,48])
a.sort()
a

a = np.ones((2,2))
b = np.array([(-1,1),(-1,1)])
a
b
result_dot = np.dot(a, b)
print(result_dot)
result_at = a@b
print(result_at)

a = np.array([1,2,3])
b = np.array([4,5,6])
a + b

a = np.array([(1,2), (2,2), (3,3), (4,4)])
b = np.array([-1,1])
a + b

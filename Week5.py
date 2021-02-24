#numpy

#library for scientific computing

#same type of elements

import numpy as np

a = np.array([1,2,3,4,5])
print(a)

print(a.size)       #prints the size of the array
print(type(a))
print(a.dtype)          #prints the type of the array

print(a.ndim)       #prints the dimension of the array

print(a.shape)

b = np.array([11.3, 54.2, 22.44])
print(type(b))
print(b.dtype)
print(a[2:4])
c = a[3:5] = 100 , 200      #changes the specific indices
print(a)


#normal code for vector addition

u = [1,0]
v = [0,1]
z = []

for n , m in zip(u,v):
    z.append(n+m)
print(z)

#numpy code for vector addition

u = np.array([1,0])
v = np.array([0,1])
z = u+v
print(z)

#vector subtraction

u = [1,0]
v = [0,-1]
z = []

for n , m in zip(u,v):
    z.append(n-m)
print(z)




u = np.array([1,0])
v = np.array([0,-1])

z = u-v
print(z)

#vector multiplication one scalar one vector

y = [1,2]
z =[]
for n in y:
    z.append(2*n)
print(z)


u = np.array([1,2])
z = 2*u
print(z)

#multiplication of two arrays

a = [1,2]
b = [1, 3]
z = []

for n, m in zip(a,b):
    z.append(n*m)
print(z)

a = np.array([2,3])
b = np.array([3,4])
z = a * b
print(z)

#taking the dot product of two arrays

a = np.array([1,3])
b = np.array([2, 4])

z = np.dot(a , b)
print(z)

#adding constant to an numpy array

a = np.array([3,4])
b = a + 1
print(b)        #braodcasting

#universal functions

#calculating the mean or average of the array

a = np.array([3,7,-8,1])
print(a.mean())

#finding the maximum and minimum

a = np.array([4,88,12,99])
print(a.max())

a = np.array([4,88,12,99])
print(a.min())

#finding the sum a
a = np.array([4,88,12,99])
print(a.sum())

print(np.pi)

x = np.array([0 , np.pi/2, np.pi])
print(x)

print(np.sin(90))

#plotting mathematical functions using linespace

#linespace returns evenly spaced numbers over a specified intervals

print(np.linspace(-2, 2 , num= 5))
print(np.linspace(-2, 2 , num= 9))

'''x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

import matplotlib.pyplot as plt
#print(plt.plot(x,y))
plt.plot(x,y)
'''
data = np.random.randn(2,3)   #Return a random matrix with data from the "standard normal" distribution.
print(data)
print(data*10)
print(data+data)
print(data.shape)
print(data.dtype)  #dtype stands for data type
print(data.size)
print(data.ndim)

#numpy ndarray for homogeneous data
ndimarray = np.array([[1,7,8], [9,4,3]])
print(ndimarray)
print(ndimarray.ndim)
print(ndimarray.shape)
print(ndimarray.size)
print(ndimarray.dtype)

print(np.zeros(10))
print(np.zeros((3,6)))

print(np.empty((2,3,2)))

print(np.arange(15))

print(np.ones([3,3], dtype=int))

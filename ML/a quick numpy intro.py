import numpy as np

#a quick numpy intro
# we vectorize in numpy with np.arange

diams = np.arange(10, dtype='float') #diams instead of becoming a list, becomes an ndarray (arrays)
areas = np.pi * (diams/2) ** 2
print(diams)
print(areas)

# a few constructors to nparrays
print(np.arange(10))
print(np.arange(10, dtype='float'))
print(np.arange(0, 10, 1.))
print(np.arange(0, 1, .1))

print(np.linspace(1, 10))


############################################
# multiplying scalar by ndarray (broadcasting)

x = np.arange(1, 4, dtype='float')
y = np.arange(4, 7, 1)
print("x: ", x)
print("y: ", y)
print("sum: ", (x + y))
print("quotient: ", (x/y))
print("differences: ", (x-y))


# nesting ndarrays
x = np.arange(10)
y = np.arange(10, 20)
z = np.vstack((x, y)) # one of many ways to assemble multidimensional arrays

print("dimensions of z: ", z.ndim)
print("shape of z: ", z.shape)
print(z)
print(z[:, 2])

# ones and zeros constructors

x = np.ones((10, 10))
y = np.zeros((10, 10))  # passing with a tuple describes the shape of the desired array
y_but_ones = np.ones_like(y)

print (x)
print(y)
print(y_but_ones)

x = np.identity(4)
print(x)
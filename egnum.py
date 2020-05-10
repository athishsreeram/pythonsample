import numpy as np
 
array1d = np.array([1, 2, 3, 4, 5, 6])
array2d = np.array([[1, 2, 3], [4, 5, 6]])
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
 
print(array1d)
 
print("-" * 10)
print(array2d)
 
print("-" * 10)
print(array3d)
 

ara1 = np.array([[1, 2], [4, 5]])
ara2 = np.array([1, 2])

c = np.linalg.solve(ara1,ara2)


print(c)
import numpy as np

random_num = np.random.randint(1, 101, size=(4, 4))
arr_max = np.max(random_num, axis=1)

print("4D array:")
print(random_num)
print("Maxima of array:")
print(arr_max)

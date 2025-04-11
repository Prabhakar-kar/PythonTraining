import numpy as np

def convert_float(arr):
    float_arr = [float(element) for element in arr]
    return float_arr

arr = np.array([1, 2, 3, 4, 5])
float_arr = convert_float(arr)

print(float_arr)

import numpy as np

if __name__ == '__main__':
    a = np.arange(3).reshape(3, 1)
    print(a)
    arr = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    a = np.insert(a, 1, arr[2], 1)
    print(a)

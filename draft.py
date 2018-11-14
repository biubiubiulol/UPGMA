import numpy as np

if __name__ == '__main__':
    a = np.array([[1, 1], [2, 2], [3, 3]])
    print(a)
    arr = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    a = np.insert(a, len(a) - 1, arr[2], 1)
    print(a)

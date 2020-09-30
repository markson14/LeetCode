import numpy as np
np.random.seed(1212)
"""
1. select 
"""


def insertionSort(l) -> list:
    n = len(l)
    for i in range(1, n):
        preindex = i-1
        cur = l[i]
        print(l, preindex)
        while preindex >= 0 and l[preindex] > cur:
            l[preindex+1] = l[preindex]
            preindex -= 1
        l[preindex+1] = cur
    return l


if __name__ == '__main__':
    """
        平均时间复杂度：O(n^2)
        最好情况：O(n)
        最坏情况：O(n^2)
        空间复杂度：O(1)
        排序方式：In-place
        稳定性：稳定
    """
    print()
    l = np.random.random_integers(0, 100, 20)
    print('unsorted: {}'.format(l))
    print()
    print('sorted: {}'.format(insertionSort(l)))

"""
    快速排序：
        1.首先L0为基准值
        2.小于pivot的移项pivot左边，大于pivot的移项pivot右侧。
        3.然后在对pivot左右两个区间
        4.左右区间重复1,2,3知道区间长度等于1
"""
import numpy as np
np.random.seed(1212)


def quick_sort(nlist):
    first, last = 0, len(nlist)-1
    quick_sort_helper(nlist, first, last)


def quick_sort_helper(nlist, first, last):
    if first < last:
        # 选择分裂点，分裂点左区间小于分裂点，右区间大于分裂点
        splitpoint = partition(nlist, first, last)
        # 对分裂点的左区间做快排
        quick_sort_helper(nlist, first, splitpoint-1)
        # 对分裂点的右区间做快排
        quick_sort_helper(nlist, splitpoint+1, last)


def partition(nlist, first, last):
    # 选择L0作为基准点
    pivot = nlist[first]
    # 左，右index选择
    left, right = first+1, last
    while True:
        # loop从左寻找比基准点大的值
        while left <= right and nlist[left] <= pivot:
            left += 1
        # loop从右寻找比基准点小的值
        while left <= right and nlist[right] >= pivot:
            right -= 1
        # 如果左比右大，证明右半边都比基准点大，退出
        if left > right:
            break
        # 否则，交换左，右index的值并继续loop
        else:
            nlist[left], nlist[right] = nlist[right], nlist[left]
    # 交换基准点的值和右index，使得右区间比基准点大，左半边比基准点小
    nlist[first], nlist[right] = nlist[right], nlist[first]
    # 返回splitpoint
    return right


if __name__ == '__main__':
    """
        平均时间复杂度：O(nlogn)
        最好情况：O(nlogn)
        最坏情况：O(n^2)
        空间复杂度：O(logn)
        排序方式：In-place
        稳定性：不稳定
    """
    print()
    l = np.random.random_integers(0, 100, 20)
    print(l)
    print()
    quick_sort(l)
    print(l)

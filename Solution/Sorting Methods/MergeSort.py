"""
    归并排序，基本思想是divide and conquer
"""
import numpy as np
np.random.seed(1212)


def merge_sort(nlist):
    n = len(nlist)
    # 如果区间小于2，则直接返回
    if n < 2:
        return nlist
    # 计算中心点
    mid = n//2
    # 对左区间做merge sort递归
    left = merge_sort(nlist[:mid])
    # 对右区间做merge sort递归
    right = merge_sort(nlist[mid:])
    # 对左右区间做merge操作
    return merge(left, right)


def merge(left, right):
    res = []
    l, r = 0, 0
    # 当左右index小于左右区间长度
    while l < len(left) and r < len(right):
        # 比较左右index值的大小，并加入空list
        if left[l] > right[r]:
            res.append(right[r])
            r += 1
        else:
            res.append(left[l])
            l += 1
    # 将剩余部分添加进list
    res.extend(left[l:])
    res.extend(right[r:])

    return res


if __name__ == '__main__':
    """
        平均时间复杂度：O(nlogn)
        最好情况：O(nlogn)
        最坏情况：O(nlogn)
        空间复杂度：O(n)
        排序方式：In-place
        稳定性：稳定
    """
    print()
    l = np.random.random_integers(0, 100, 20)
    print(l)
    print()
    print(merge_sort(l))

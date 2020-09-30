"""
    堆
    1. 符合完全二叉树
    2. 父节点大于字节点

    堆排序，利用堆的特性，每次堆顶与末尾值交换，并将末尾值pop出来，
    然后再对堆顶做一次heapify操作从而获得一个新的堆。然后loop操作
    直到堆为空。
"""
import numpy as np
np.random.seed(1212)


def heapify(nlist, n, i):
    # 如果index大于list长度，则退出
    if i >= n:
        return
    # 父节点选取
    root = i
    # 字节点选取，可以通过完全二叉树性质计算得出
    child1 = 2*i+1
    child2 = 2*i+2
    # 比较父节点与子节点大小
    if child1 < n and nlist[child1] > nlist[root]:
        root = child1
    if child2 < n and nlist[child2] > nlist[root]:
        root = child2
    # 如果父节点index与初始不一致
    if root != i:
        # 交换父节点与最大子节点
        nlist[root], nlist[i] = nlist[i], nlist[root]
        # 对子节点继续做heapify操作
        heapify(nlist, n, root)


def build_heap(nlist, n):
    last = (n-1) // 2
    # 从完全二叉树的倒数第二行开始做heapify操作
    for i in range(last, -1, -1):
        heapify(nlist, n, i)


def heap_sort(nlist):
    n = len(nlist)
    # 建立堆
    build_heap(nlist, n)
    # 从末尾开始遍历
    for i in range(n-1, -1, -1):
        # 交换堆顶和末尾值
        nlist[i], nlist[0] = nlist[0], nlist[i]
        # 对堆顶做heapify操作，忽略最末尾已经输出的值。所以这里的i是不断减小的
        heapify(nlist, i, 0)


if __name__ == '__main__':
    """
        平均时间复杂度：O(nlogn)
        最好情况：O(nlogn)
        最坏情况：O(nlogn)
        空间复杂度：O(1)
        排序方式：In-place
        稳定性：稳定
    """
    print()
    l = np.random.random_integers(0, 100, 20)
    print(l)
    heap_sort(l)
    print(l)

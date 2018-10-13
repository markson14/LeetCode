def func(list_):
    for cur in range(len(list_)-1):
        min_ = cur
        for i in range(cur+1,len(list_)):
            if list_[i] < list_[min_]:
                min_ = i
        list_[cur], list_[min_] = list_[min_], list_[cur]
    return list_

if __name__ == '__main__':
    """
        平均时间复杂度：O(n^2)
        最好情况：O(n)
        最坏情况：O(n^2)
        空间复杂度：O(1)
        排序方式：In-place
        稳定性：不稳定
    """
    print()
    l = [2,3,5,6,3,2,1,3,4,5,6,7,8,5,4,1,3,4]
    print('unsorted: {}'.format(l))
    print()
    print('sorted: {}'.format(func(l)))
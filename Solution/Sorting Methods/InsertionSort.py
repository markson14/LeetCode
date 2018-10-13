def func(l) -> list:
    n = len(l)
    for i in range(1,n):
        preindex = i-1
        cur = l[i]
        while preindex>=0 and l[preindex] > cur:
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
    l = [2,3,5,6,3,2,1,3,4,5,6,7,8,5,4,1,3,4]
    print('unsorted: {}'.format(l))
    print()
    print('sorted: {}'.format(func(l)))
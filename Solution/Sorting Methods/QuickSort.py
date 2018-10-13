"""
    快速排序：
        1.首先L0为基准值
        2.小于pivot的移项pivot左边，大于pivot的移项pivot右侧。
        3.然后在对pivot左右两个区间
        4.左右区间重复1,2,3知道区间长度等于1
"""
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    return alist

def quickSortHelper(alist,first,last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark

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
    l = [2,3,5,6,3,2,1,3,4,5,6,7,8,5,4,1,3,4]
    print(l)
    print()
    print(quickSort(l))
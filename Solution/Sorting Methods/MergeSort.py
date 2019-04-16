"""
    归并排序，基本思想是divide and conquer
"""

def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
def Merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

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
    l = [2,3,5,6,3,2,1,3,4,5,6,7,8,5,4,1,3,4]
    print(l)
    print()
    print(MergeSort(l))
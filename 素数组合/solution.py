import sys
def prime(n,l): ## 埃氏筛法
    flag = [1]*(n+2)
    p=2
    while(p<=n):
        l.append(p)
        for i in range(2*p,n+1,p):
            flag[i] = 0  ## 把p的倍数都变成0
        while 1:
            p += 1
            if(flag[p]==1): ## 判断是否1。如果是，则为素数。跳出while 1的循环
                break
n = 10
l=[]
prime(n,l)
count_ = 0
for i in l:
    left_ = n - i
    if left_ in l:
        l.remove(left_)
        count_ += 1
print(count_)
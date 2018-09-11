while True:
    try:
        n = int(input())
        l = list(map(int,input().split()))
        sum_,max_ = 0,l[0]
        for i in l:
            if sum_ >= 0:
                sum_ += i
            else:
                sum_ = i
                
            if sum_ > max_:
                max_ = sum_
        print(max_)
    except:
        break

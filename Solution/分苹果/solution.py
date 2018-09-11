def splitapple(n,p):
    if sum(p) % n != 0:
        return -1
    avg = sum(p)/n
    c = 0
    for i in p:
        if (i-avg)%2 != 0:
            return -1
        elif i > avg:
            c += i- avg
    return int(c/2)

n = int(input())
p = list(map(int ,input().split()))
print(splitapple(n,p))
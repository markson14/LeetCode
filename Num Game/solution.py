a = int(input())
list_ = sorted([int(b) for b in input().split()])
basis = 0
for i in range(a):
    if list_[i] > basis+1:
        break
    else:
        basis += list_[i]
print(basis+1)
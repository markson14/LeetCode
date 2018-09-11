def fib(n):
    result_list = []
    a, b = 0, 1
    while n > 0:
        result_list.append(b)
        a, b = b, a + b
        n -= 1
    return result_list[-1]
 
num_ = int(input())
opt = 0
for i in range(1,31):
    if fib(i) > num_:
        print(min(abs(fib(i)-num_), abs(fib(i-1)-num_)))
        break
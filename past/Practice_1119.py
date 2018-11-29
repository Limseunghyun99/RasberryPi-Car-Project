def RecurHanoi(n):
    if n == 1:
        return 1
    else:
        return 2*RecurHanoi(n-1) + 1

print(RecurHanoi(10))

def func(n):
    cnt = 0
    while(True):
        cnt += 1
        n -= 1

        if n<0 :
            break

    return cnt

print(func(10))
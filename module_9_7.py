def is_prime(func):
    def  wrapper(a, b, c):
        x = func(a, b, c)
        flag = True
        for i in range(2, (x // 2) + 1):
            if x % i == 0:
                flag = False
        flag = True
        if flag:
            print('Простое')
        else:
            print('Непростое')
        return x
    return wrapper
@is_prime
def sum_three(a, b, c):
    s = a + b + c
    return s
result = sum_three(2, 3, 6)
print(result)
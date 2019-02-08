def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    init = [1, 2]
    gen_fib = (sum(init[-2:]) for _ in range(n-2))
    for v in gen_fib:
        init.append(v)
    return init[-1]    

a = input()
print(fib(a))
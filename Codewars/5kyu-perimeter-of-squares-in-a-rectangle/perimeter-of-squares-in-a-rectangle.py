def perimeter(n):
    init = [1, 1]
    fib = (sum(init[-2:]) for _ in range(n-1))
    for v in fib:
        init.append(v)
    return sum(init)*4

n = 5
print(perimeter(n))

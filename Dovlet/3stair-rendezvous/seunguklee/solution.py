a, b = map(int, input().split())

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

print((a + b) // gcd(a, b))

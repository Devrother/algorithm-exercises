def solution2(n):
	if (n == 1 or n == 2 or n == 3):
		return n
	
	a, b = 2, 3
	for _ in range(3, n):
		a, b = b, (a + b) % 1234567

	return b



# 그냥 해본 제네레이터.
# 위 함수에 비해 약 2배 가량 느리다. 함수 호출 때문에 그런듯 하다.
def fib_gen(n):
	a, b = 1, 2
	for _ in range(n):
		yield a
		a, b = b % 1234567, a + b

def solution(n):
	res = 0

	for v in fib_gen(n):
		res = v
		
	return res

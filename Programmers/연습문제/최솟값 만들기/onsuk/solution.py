def solution(A, B):
    A.sort()
    B.sort(reverse = True)
    # return sum([A[i] * B[i] for i in range(len(A))])
    return sum(a * b for a, b in zip(A, B))

A = [5, 2, 6]
B = [2, 3, 1]

print(solution(A, B))
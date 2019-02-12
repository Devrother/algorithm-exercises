def binary(num, n):
    for i in range(n):
        if (num >> i) & 1:
            yield '#'
        else:
            yield ' '

def solution(n, arr1, arr2):
    answer = []

    for e in [a1 | a2 for a1, a2 in zip(arr1, arr2)]:
        s = [v for v in binary(e, n)]
        s.reverse()
        answer.append(''.join(s))
    
    return answer

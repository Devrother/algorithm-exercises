class Solution:
    def largestPerimeter(self, A):
        A.sort()
        A.reverse()
        for _ in range(len(A)):
            while((len(A)>2)):
                if A[0] < (A[1]+A[2]):
                    return sum(A[:3])
                else:
                    del A[0]
        return 0
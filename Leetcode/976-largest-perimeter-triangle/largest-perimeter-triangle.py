class Solution:
    def largestPerimeter(self, A):
        A.sort(reverse=True)
        while((len(A)>2)):
            if A[0] < (A[1]+A[2]):
                return sum(A[:3])
            else:
                A.pop(0)
        return 0
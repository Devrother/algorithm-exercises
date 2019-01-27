
class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # a + b > c
        
        sort_a = sorted(A, reverse=True)
        for i in range(0, len(A) - 2):
            if sort_a[i] < sort_a[i + 1] + sort_a[i + 2]:
                return sort_a[i] + sort_a[i + 1] + sort_a[i + 2]
        return 0

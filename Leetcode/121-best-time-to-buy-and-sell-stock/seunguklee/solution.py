class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        buy, max_p = prices[0], 0
        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            else:
                max_p = max(max_p, prices[i] - buy)
        return max_p

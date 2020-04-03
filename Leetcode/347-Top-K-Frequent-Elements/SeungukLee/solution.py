from collections import Counter

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hq = []
        for num, frequent in Counter(nums).items():
            heapq.heappush(hq, (-frequent, num))
        
        return [heapq.heappop(hq)[1] for _ in range(k)]

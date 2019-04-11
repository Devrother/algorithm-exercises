from collections import defaultdict

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in dislikes:
            adj_list[v].append(u)
            adj_list[u].append(v)
        # [[1,2],[1,3],[2,4]]
    
#         adj_list ={
#             1: [2, 3]
#             2: [1, 4]
#             3: [1]
#             4: [2]
#         }
        
        color = {}
        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
        
            return all(dfs(nei, c^1) for nei in adj_list[node])
        
        # return dfs(1) 해버리면 [[1,2],[3,4],[4,5],[3,5]] 테스트 케이스 통과못함
#         1 - 2

#         3 - 4
#           \ |
#             5
        return all(dfs(node) for node in range(1, N+1) if node not in color)


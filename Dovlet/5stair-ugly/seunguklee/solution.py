import heapq
 
 
def ugly(n):
    if n == 1:
        return 1
 
    p_list = [2, 3, 5]
    heap = p_list + [1]
    cnt = n
    heapq.heapify(heap)
 
    while cnt > 1:
        num = heapq.heappop(heap)
        for p in p_list:
            ugly_num = p * num
            if ugly_num not in heap:
                heapq.heappush(heap, ugly_num)
        cnt -= 1
 
    return "The {0}'th ugly number is {1}.".format(n, heapq.heappop(heap))
 
 
a = int(input())
print(ugly(a))

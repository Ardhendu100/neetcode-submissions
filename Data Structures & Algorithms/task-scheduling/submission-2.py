from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        seen = {}
        for i in tasks:
            seen[i] = seen.get(i, 0) + 1
        heap = [-val for val in seen.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time+=1
            if not heap:
                time = q[0][1]
            else:
                val = heapq.heappop(heap)
                
                if abs(val) > 1:
                    q.append([val+1, time+n])
            if q and time == q[0][1]:
                heapq.heappush(heap, q.popleft()[0])
        return time



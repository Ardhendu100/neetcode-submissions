class MedianFinder:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        self.l = len(self.heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        self.l = len(self.heap)
        

    def findMedian(self) -> float:
        if self.l == 0:
            return 0
        elif self.l == 1:
            return self.heap[0]
        elif self.l % 2 == 1:
            return self.heap[self.l // 2]
        else:
            middle1 = self.heap[(self.l // 2) - 1]
            middle2 = self.heap[self.l // 2]
            return (middle1 + middle2) / 2


        
        
        
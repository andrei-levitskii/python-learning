from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.max_heap_for_smallnum = []
        self.min_heap_for_largenum = []

    def addNum(self, num: int) -> None:
        if not self.max_heap_for_smallnum or -self.max_heap_for_smallnum[0] >= num:
            heappush(self.max_heap_for_smallnum, -num)
        else:
            heappush(self.min_heap_for_largenum, num)
        if len(self.max_heap_for_smallnum) > len(self.min_heap_for_largenum) + 1:
            heappush(self.min_heap_for_largenum, -heappop(self.max_heap_for_smallnum))
        elif len(self.max_heap_for_smallnum) < len(self.min_heap_for_largenum):
            heappush(self.max_heap_for_smallnum, -heappop(self.min_heap_for_largenum))

    def findMedian(self) -> float:
        if len(self.max_heap_for_smallnum) == len(self.min_heap_for_largenum):
            return -self.max_heap_for_smallnum[0] / 2.0 + self.min_heap_for_largenum[0] / 2.0
        return -self.max_heap_for_smallnum[0] / 1.0


def main() -> None:
    medianFinder = MedianFinder()
    medianFinder.addNum(1)  # arr = [1]
    medianFinder.addNum(2)  # arr = [1, 2]
    print(medianFinder.findMedian())  # return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3)  # arr[1, 2, 3]
    print(medianFinder.findMedian())  # return 2.0


if __name__ == "__main__":
    main()

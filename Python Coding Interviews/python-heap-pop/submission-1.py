import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    heapnew=[]
    # for i in range(len(heap)):
    #     a=heapq.heappop(heap)
    #     heapq.heappush(heapnew,a)
    # return heapnew
    while heap:
        heapnew.append(heapq.heappop(heap))
    return heapnew



# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))

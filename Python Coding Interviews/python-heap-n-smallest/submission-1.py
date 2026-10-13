import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    arr1=[]
    arr1=heapq.nsmallest(1,arr)
    return arr1[0]



def get_min_4_elements(arr: List[int]) -> List[int]:
    return heapq.nsmallest(4,arr)


def get_min_2_elements(arr: List[int]) -> List[int]:
    # result=[]
    # arr=heapq.nsmallest(2,arr)
    # for num in arr:
    #     pair=(-num,num)
    #     heapq.heappush(result,pair)
    
    # results=[]
    # while result:
    #     pair=heapq.heappop(result)
    #     original_num=pair[1]
    #     results.append(original_num)
    # return results
    arr=heapq.nsmallest(2,arr)
    return arr[::-1]

# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))


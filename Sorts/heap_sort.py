from heapq import heappop, heappush
import time
import random
start_time = time.time()


def heap_sort(arr) :
    heap = []
    for item in arr:
        
        heappush(heap,item)
    # print( heap)

    ordered = []

    while heap :
        # print(heap)
        ordered.append(heappop(heap))

    return ordered

# print(res)
arr = random.sample(range(1,20),16)
print(heap_sort(arr))

print("--- %s seconds ---" % (time.time() - start_time))

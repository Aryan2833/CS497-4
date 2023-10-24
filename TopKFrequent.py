from collections import Counter
import heapq


def kMostFrequent(nums, k):
    count = Counter(nums)
    heap = []

    for num, freq in count.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        else:
            if freq > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, num))
    result = [x[1] for x in heap]

    return result


# Test cases
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(kMostFrequent(nums1, k1))

nums2 = [1]
k2 = 1
print(kMostFrequent(nums2, k2))

import heapq
def peekTopK(arr, k):
    topK = []
    minHeap = []

    for i in range(k):
        heapq.heappush(minHeap, -arr[i])

    for i in range(k):
        current = -heapq.heappop(minHeap)
        topK.append(current)

        leftChildIndex = 2 * i + 1
        rightChildIndex = 2 * i + 2

        if leftChildIndex < len(arr):
            heapq.heappush(minHeap, -arr[leftChildIndex])
        if rightChildIndex < len(arr):
            heapq.heappush(minHeap, -arr[rightChildIndex])

    return topK

# Test case
arr = [15, 13, 12, 10, 8, 9]
k = 5
result = peekTopK(arr, k)
print(result)

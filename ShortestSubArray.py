def shortestSubarraySumAtLeastK(nums, k):
    n = len(nums)
    min_length = float('inf')
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    indices = []

    for i in range(n + 1):
        while indices and prefix_sum[i] - prefix_sum[indices[0]] >= k:
            min_length = min(min_length, i - indices.popleft())

        while indices and prefix_sum[i] <= prefix_sum[indices[-1]]:
            indices.pop()

        indices.append(i)

    return min_length if min_length != float('inf') else -1

# Test cases
nums1 = [1]
k1 = 1
print(shortestSubarraySumAtLeastK(nums1, k1))

nums2 = [1, 2]
k2 = 4
print(shortestSubarraySumAtLeastK(nums2, k2))

nums3 = [2, -1, 2]
k3 = 3
print(shortestSubarraySumAtLeastK(nums3, k3))

def kthSmallestPrimeFraction(arr, k):
    def countFractions(x):
        count = 0
        left, right = 0, 1
        maxFraction = 0
        for j in range(1, len(arr)):
            while arr[left] < x * arr[j]:
                left += 1
            count += j - left
            if left > 0:
                fraction = arr[left - 1] / arr[j]
                if fraction > maxFraction:
                    maxFraction = fraction
                    maxFractionIndices = (left - 1, j)
        return count, maxFractionIndices

    left, right = 0, 1
    while True:
        mid = (left + right) / 2
        count, maxFractionIndices = countFractions(mid)
        if count == k:
            return [arr[maxFractionIndices[0]], arr[maxFractionIndices[1]]]
        elif count < k:
            left = mid
        else:
            right = mid

# Test cases
arr1 = [1, 2, 3, 5]
k1 = 3
print(kthSmallestPrimeFraction(arr1, k1))  # Output: [2, 5]

arr2 = [1, 7]
k2 = 1
print(kthSmallestPrimeFraction(arr2, k2))  # Output: [1, 7]

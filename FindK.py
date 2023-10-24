def findClosestElements(arr, k, x):
    left, right = 0, len(arr) - k

    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]


# Test cases
arr1 = [1, 2, 3, 4, 5]
k1 = 4
x1 = 3
print(findClosestElements(arr1, k1, x1))

arr2 = [1, 2, 3, 4, 5]
k2 = 4
x2 = -1
print(findClosestElements(arr2, k2, x2))

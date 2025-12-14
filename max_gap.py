def merge(nums, l, m, h):
    result = []
    i, j = l, m + 1

    # Merge two sorted halves
    while i <= m and j <= h:
        if nums[i] <= nums[j]:
            result.append(nums[i])
            i += 1
        else:
            result.append(nums[j])
            j += 1

    # Copy remaining elements
    while i <= m:
        result.append(nums[i])
        i += 1
    while j <= h:
        result.append(nums[j])
        j += 1

    # Copy back to nums
    for k in range(len(result)):
        nums[l + k] = result[k]


def merge_sort(nums, l, h):
    if l < h:
        m = (l + h) // 2
        merge_sort(nums, l, m)
        merge_sort(nums, m + 1, h)
        merge(nums, l, m, h)


def maximumGap(nums):
    n = len(nums)
    if n < 2:
        return 0

    merge_sort(nums, 0, n - 1)

    # Print sorted array (like your C code)
    print("Sorted:", nums)

    max_gap = 0
    for i in range(n - 1):
        r = nums[i + 1] - nums[i]
        if r > max_gap:
            max_gap = r

    return max_gap


# Example usage
arr = [3, 6, 9, 1]
print("Maximum Gap:", maximumGap(arr))

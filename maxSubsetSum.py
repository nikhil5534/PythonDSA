def maxsum(arr, k):
    if not arr or k <= 0:
        return 0
    n = len(arr)
    if k > n:
        return None
    max_sum = float('-inf')
    window_sum = 0
    for i in range(k):
        window_sum += arr[i]
        max_sum = max(max_sum, window_sum)
    for i in range(k, n):
        window_sum -= arr[i-k]
        window_sum += arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum


arr = [23, 5, 4, 3, 1, 11, 67, 56, 34, 54]
k = 3
print(maxsum(arr, k))
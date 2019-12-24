
def longestIncreasingSubsequence(arr):
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] >= arr[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)



arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(longestIncreasingSubsequence(arr))
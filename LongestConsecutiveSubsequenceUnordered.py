
def longest_consecutive_subsequence_unordered(arr):
    arr_set = set(arr)
    longest = 0
    for num in arr:
        if (num-1 not in arr_set):
            cur = num
            count = 1
            while(cur+1 in arr_set):
                count += 1
                cur += 1
            longest = max(longest, count)

    return longest

arr = [-20, 1, -24, -23, 2]
print longest_consecutive_subsequence_unordered(arr)

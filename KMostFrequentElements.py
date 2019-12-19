
def get_frequency_lookup_array(arr):
    lookup_array = []
    freq_map = {}
    for i, n in enumerate(arr):
        if n in freq_map:
            freq_map[n] += 1
        else:
            freq_map[n] = 1
        lookup_array.append([])
    lookup_array.append([])
    for key, val in freq_map.items():
        lookup_array[val].append(key)
    return lookup_array

def kMostFrequentElements(arr, k):
    frequency_lookup_arr = get_frequency_lookup_array(arr)
    result = []
    for bucket in reversed(frequency_lookup_arr):
        for v in bucket:
            if k <= 0:
                return result
            result.append(v)
            k -= 1

    return result

arr = [1, 6, 2, 6, 1, 6, 1]
k = 4

result = kMostFrequentElements(arr, k)
print result
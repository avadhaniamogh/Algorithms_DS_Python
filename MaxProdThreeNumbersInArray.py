def max_prod(arr):
    min1 = float('inf')
    min2 = float('inf')

    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')

    for num in arr:
        if num <= min1:
            min2 = min1
            min1 = num
        elif num <= min2:
            min2 = num

        if num >= max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num >= max2:
            max3 = max2
            max2 = num
        elif num >= max3:
            max3 = num

    return max(max1*max2*max3, max1*min1*min2)

arr = [1,-2,-3,4]
print max_prod(arr)

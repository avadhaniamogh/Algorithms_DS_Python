def longestCommonSubstring(X, Y, m, n, res):
    if m <= 0 or n <= 0:
        return 0
    elif X[m-1] == Y[n-1]:
        res = longestCommonSubstring(X, Y, m-1, n-1, res+1)
    return max(res, longestCommonSubstring(X, Y, m-1, n, 0), longestCommonSubstring(X, Y, m, n-1, 0))


X = "abcdaf"
Y = "zbcdf"

print "Length of LCS is ", longestCommonSubstring(X , Y, len(X), len(Y), 0)
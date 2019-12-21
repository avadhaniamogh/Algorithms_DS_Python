def lcs(X, Y, m, n):
    if m <= 0 or n <= 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m-1, n), lcs(X, Y, m, n-1))


def lcs_tabulation(X, Y):
    m = len(X)
    n = len(Y)

    dp = [[None for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i <= 0 or j <= 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


X = "AGGTAB"
Y = "GXTXAYB"

print "Length of LCS is ", lcs(X , Y, len(X), len(Y))
print "Length of LCS table is ", lcs_tabulation(X , Y)


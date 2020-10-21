while True:
    n = int(input())
    a = list(map(int, input().split()))

    MOD = 10 ** 9 + 7

    dp = [[0 for j in range(n+1)] for i in range(n+1)]
    dp[1][1] = 1

    for i in range(2, n+1):
        for j in range(1, i+1):

            if a[i-2]:
                dp[i][j] += dp[i][j-1] + dp[i-1][j-1]
                dp[i][j] %= MOD

            else:
                dp[i][j] += dp[i][j-1] + dp[i-1][i-1] - dp[i-1][j-1]
                dp[i][j] %= MOD

    print(dp[n][n])



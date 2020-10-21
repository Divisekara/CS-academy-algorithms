dp = [[0 for j in range(5)] for i in range(5)]

dp[1][1] = 1000

for i in range(0,len(dp)):

    for j in range(0,len(dp)):
        if(dp[i][j]):
            print('fucking awesome')
        else:
            print(i,j)

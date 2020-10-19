# n = int(input().strip())
# L = list(map(int, input().strip().split(" ")))
 
# current_sum = -(10**10) #sum(list(map(abs, L))) * (-1)

# for i in range(1,n):

#     for j in range((i+1)%2, i, 2):
#         total = sum(L[j:i+1])

#         current_sum = max(current_sum, total)

# print(current_sum)


n = int(input())
a = list(map(int,input().split(' ')))

dp = [0 for i in range(n+2)]

mx = -2 * 10 ** 9
for i in range(n-2,-1,-1):
    dp[i] = a[i] + a[i+1] + dp[i+2]
    mx = max(mx, dp[i])
    dp[i] = max(0,dp[i])

print(mx)

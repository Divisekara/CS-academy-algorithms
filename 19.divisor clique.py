n = int(input().strip())

L = sorted(list(map(int, input().strip().split())))

best = [0] * (n)

for i in range(n):
    
    currentBest = 0

    for j in range(i):
        
        if(L[i] % L[j] == 0 and currentBest<best[j]):
            currentBest =  best[j]

    best[i] = currentBest + 1

print(max(best))


# N = int(input())
# setN = list(map(int, input().split()))
# best = [0 ] * N

# setN = sorted(setN)
# for i in range(N):
#     cbest = 0
#     for j in range(i):
#         if(setN[i] % setN[j] == 0 and  cbest<best[j]):
#             cbest = best[j]
#     best[i] = cbest + 1

# print(max(best))




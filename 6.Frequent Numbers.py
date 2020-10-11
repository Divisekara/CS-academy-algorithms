n, k = list(map(int, input().strip().split(" ")))

L = list(map(int, input().strip().split()))

D = {}
for i in L:
    if(D.get(i) == None):
        D[i] = 1
    else:
        D[i] += 1
    
answer = 0
for j in list(D.values()):
    if(j>= k):
        answer+=1

print(answer)

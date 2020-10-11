n = int(input().strip())

D = {}
L = list(map(int, input().strip().split()))

for i in L:
    if(D.get(i)==None):
        D[i] = i
    else:
        D[i] +=i

answer = sum(list(D.values())) - max(list(D.values()))

print(answer)


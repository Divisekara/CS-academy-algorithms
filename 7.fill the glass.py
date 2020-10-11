n,k = list(map(int, input().strip().split()))

answer = (sum(sorted(list(map(int, input().strip().split())))[:k]))/100

if(answer - int(answer) == 0.0 ):
    print(int(answer))
else:
    print(int(answer)+1)


n, m = list(map(int, input().strip().split(" ")))

t = sorted(list(map(int, input().strip().split(" "))))
T = t[:]
t.reverse()

for i in range(n):
    a,b = sorted(list(map(int, input().strip().split(" "))))
    count = 1

    for j in T:
        if(a<=j<=b):
            count+=1

    print(count-1)



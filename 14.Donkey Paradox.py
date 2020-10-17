n,m = list(map(int, input().strip().split(" ")))
r1, c1 = list(map(int, input().strip().split(" ")))
r2, c2 = list(map(int, input().strip().split(" ")))

count = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        total_h1 = abs(r1-i) +abs(c1-j)
        total_h2 = abs(r2-i) +abs(c2-j)
        if(total_h1==total_h2):
            count +=1
    
print(count)




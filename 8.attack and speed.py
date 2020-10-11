a,s,k,x,y = list(map(int, input().strip().split()))

#Find n
n = (s - a + k*y) / (x + y)

if(n - int(n) == 0):
    print(int(n))
else:
    print(-1)


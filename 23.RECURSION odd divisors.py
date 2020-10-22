n = int(input().strip())

    
def f(n):
    if(n==0):
        return 0
    total = 0

    k = (n+1)//2

    total += k**2

    total += f(n//2)

    return total
        


for i in range(0,n):
    a,b = list(map(int, input().strip().split()))

    print(f(b) - f(a-1))


     
    
    


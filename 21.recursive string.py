n, k =list(map(int, input().strip().split(" ")))

def f(n):
    if(n == 0):
        return "a"
    if(n == 1):
        return 'b'
    if(n == 2):
        return 'c'

    a = 'a'
    b = 'b'
    c = 'c'

    for i in range(2,n):
        a,b,c = b,c, a+b+c
    
    return c

word = f(n) 
if(len(word) < k ):
    print(-1)
else:
    print(word[k-1])

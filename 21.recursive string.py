n, k =list(map(int, input().strip().split(" ")))

def f(n):
    if(n == 0):
        return "a"
    if(n == 1):
        return 'b'
    if(n == 2):
        return 'c'
    return f(n-1) + f(n-2) + f(n-3)

print(f(n)[k-1])

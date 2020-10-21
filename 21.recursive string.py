n, k =list(map(int, input().strip().split(" ")))


length = [0] * (n+1)
length[0:3] = [1,1,1]

for i in range(3, n+1):
    length[i] = length[i-1] + length[i-2] + length[i-3]


def f(n,k, length):
    if (length[n]<k):
        return -1

    if(n == 0):
        return 'a'

    elif(n == 1):
        return 'b'

    elif(n == 2):
        return 'c'

    for i in range(1,4):
        if(k > length[n-i]):
            k -= length[n-i]
        else:
            return f(n-i, k, length)

print(f(n,k, length))

# else:
#     a = 'a'
#     b = 'b'
#     c = 'c'

#     for i in range(2,n):
#         a,b,c = b,c, c+b+a

#     if(len(c) < k ):
#         print(-1)
#     else:
#         print(c[k-1])




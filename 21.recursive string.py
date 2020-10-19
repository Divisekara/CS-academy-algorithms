n, k =list(map(int, input().strip().split(" ")))


if(n == 0 and k==1):
    print ("a")
elif(n == 1 and k==1):
    print ('b')
elif(n == 2 and k==1):
    print ('c')


else:
    a = 'a'
    b = 'b'
    c = 'c'

    for i in range(2,n):
        a,b,c = b,c, c+b+a

    if(len(c) < k ):
        print(-1)
    else:
        print(c[k-1])

n = int(input().strip())

L = list(map(int, input().strip().split()))

D = {'0':0, '1':0, '2':0}

for i in L:
    if (i%3==0):
        D['0'] += 1
    elif(i%3==1):
        D['1'] += 1
    else:
        D['2'] += 1

x = D['0']
y = D['1']
z = D['2']

print((x-1)*x//2 + y*z)


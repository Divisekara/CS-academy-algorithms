n = int(input().strip())
L = list(map(int, input().strip().split()))

even = 0
odd = 0

for i in L:
    if(i%2==0):
        even +=1
    else:
        odd +=1

print(even * odd)



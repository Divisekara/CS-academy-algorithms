n = int(input().strip())
L = sorted(list(map(int, input().strip().split())))

total = 0

alex = [n for n in L if n>0]

others = [n for n in L if n<=0]
others.reverse()


if(len(alex)==0):
    alex.append(others.pop(0))

if(len(others)%2==0):
    alex.append(others.pop(0))

for i in range(len(others)):
    if(i%2==1):
        alex.append(others[i])

print(sum(alex))











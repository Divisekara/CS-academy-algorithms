n = int(input().strip())

D={}
for i in range(n):
    word = "".join(sorted(input().strip()))

    if(D.get(word) == None):
        D[word] = 1
    else:
        D[word] +=1

print(max(list(D.values())))


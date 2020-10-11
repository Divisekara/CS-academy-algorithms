L = list(input().strip())

M = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(len(M)-1):
    if(L.count(M[i]) != L.count(M[i+1])):
        print(0)
        break
else:
    print(1)






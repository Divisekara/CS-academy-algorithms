n = int(input().strip())

L= [] 

for i in range(1, n+1):
    lmnt = input()
    L.append((lmnt, i))


li = sorted(L, key=lambda x: x[0])

for i in li:
    print(i[1] , end = " ")









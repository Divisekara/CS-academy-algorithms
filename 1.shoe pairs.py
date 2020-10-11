n = int(input().strip())

D = {}
for i in range(n):
    size, side = input().strip().split()

    if (D.get(size)==None):
        D[size] = side

    else:
        sides = D.get(size)
        sides += side
        D[size] = sides

answer = 0 
for i in list(D.keys()):
    L = list(D[i])
    answer += min(L.count('R'), L.count('L'))

print(answer)






n = int(input().strip())
L = list(map(int, input().strip().split(" ")))

M = [0] * (n) 

for i in range(1,n):

    current_sum = sum(list(map(abs, L))) * (-1)

    for j in range((i+1)%2, i, 2):
        total = sum(L[j:i+1])

        if(current_sum < total):
            current_sum = total
    
    M[i] = current_sum

M.pop(0)
print(max(M))



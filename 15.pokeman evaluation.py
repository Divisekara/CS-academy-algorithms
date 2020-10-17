n, m, x, y = list(map(int, input().strip().split(" ")))
answer = int(n -(n-m/x) / (1 + y/x ))


if(answer>=n):
    print(n)
else:
    print(answer)

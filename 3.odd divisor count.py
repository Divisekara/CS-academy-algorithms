a,b = list(map(int, input().strip().split()))

c , d = a**0.5, b**0.5

answer=0

if (c == int(c)):
    c = int(c)
else:
    c = int(c) + 1

d = int(d)

answer = answer + d - c + 1

print(answer)
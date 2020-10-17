n = int(input().strip())
L = sorted(list(map(int, input().strip().split(" "))))

from functools import reduce

difference = lambda x,y: abs(x-y)

answer = reduce(difference, L)

print(answer)
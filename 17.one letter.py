n = int(input().strip())

answer = []
for i in range(n):
    w = sorted(list(input().strip()))[0]
    answer.append(w)

answer.sort()

print("".join(answer))
s = input().strip())
p = input().strip()

for i in s:
    print(p[ord(i)-97], end="")